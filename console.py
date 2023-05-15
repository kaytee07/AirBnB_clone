#!/usr/bin/python3
"""
This is a command interpreter for our airbnb clone
"""
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    set up the command interpreter and interpret commands input
    by user
    """
    prompt = "(hbnb) " if sys.__stdin__.isatty() else ''

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        _cmds = _clas = _ids = _args = ''

        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:
            printline = line[:]

            _clas = printline[:printline.find('.')]

            _cmds = printline[printline.find('.') + 1:printline.find('(')]
            if _cmds not in HBNBCommand.dot_cmds:
                raise Exception

            printline = printline[printline.find('(') + 1:printline.find(')')]
            if printline:
                printline = printline.partition(', ')

                _ids = printline[0].replace('\"', '')

                printline = printline[2].strip()
                if printline:
                    if printline[0] == '{' and printline[-1] == '}'\
                            and type(eval(printline)) is dict:
                        _args = printline
                    else:
                        _args = printline.replace(',', '')
            line = ' '.join([_cmds, _clas, _ids, _args])

        except Exception:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints this if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_create(self, className=None):
        """Create a new instance of the base Model"""
        if className is None:
            print("** class name missing **")

        try:
            cls = globals()[className]
        except KeyError:
            print("** class doesn't exist **")
            return
        newinstance = cls()
        newinstance.save()
        print(newinstance.id)

    def do_show(self, args):
        """ show instance based on className and ID passed"""
        new = args.partition(" ")
        class_name = new[0]
        class_id = new[2]

        if class_id and ' ' in class_id:
            class_id = class_id.partition(' ')[0]

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not class_id:
            print("** instance id missing **")
            return

        key_attr = class_name + "." + class_id
        print(key_attr)
        try:
            print(storage._FileStorage__objects[key_attr])
        except KeyError:
            print("** no instance found **")

    def do_count(self, args):
        """ count number of instances of a particular class"""
        count = 0
        for key, value in storage._FileStorage__objects.items():
            if key.split('.')[0] == args.split(' ')[0]:
                count += 1
        print(count)

    def do_destroy(self, args):
        """delete an instance of the class"""
        new = args.partition(" ")
        class_name = new[0]
        class_id = new[2]

        if class_id and ' ' in class_id:
            class_id = class_id.partition(' ')[0]

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not class_id:
            print("** instance id missing **")
            return

        key_attr = class_name + "." + class_id
        try:
            del (storage.all()[key_attr])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_update(self, args):
        """update instance based on class and id"""
        if not args:
            print("** class name missing **")
            return

        if len(args.split()) == 1:
            print("** instance id missing **")
            return

        if len(args.split()) == 2:
            print("** attribute name missing **")
            return

        if len(args.split()) == 3:
            print("** value missing **")
            return

        className, ids, attr, value = args.split()

        try:
            globals()[className]
        except KeyError:
            print("** class doesn't exist **")
            return

        storage.reload()
        all_objs = storage.all()
        keys = f"{className}.{ids}"

        try:
            found_obj = all_objs[keys]

            data_type = type(value)
            if data_type == int:
                casted_value = int(value)
            elif data_type == float:
                casted_value = float(value)
            elif data_type == str:
                casted_value = str(value)
            elif data_type == bool:
                casted_value = bool(value)
            else:
                casted_value = value

            setattr(found_obj, str(attr), casted_value)
            found_obj.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """print all instances created from the classNamepassed"""
        list_models = []

        if args:
            args = args.split(' ')[0]
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return

            for key, value in storage._FileStorage__objects.items():
                if key.split('.')[0] == args:
                    list_models.append(str(value))

        else:
            for key, value in storage.all.items():
                list_models.append(str(value))

        print(list_models)

    def do_quit(self, line):
        """exit the command interpreter"""
        return True

    def do_EOF(self, line):
        """exit the command interpreter"""
        return True

    def emptyline(self):
        """Override emptyline method to do nothing."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
