#!/usr/bin/python3
"""
This is a command interpreter for our airbnb clone
"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    set up the command interpreter and interpret commands input 
    by user
    """
    prompt = "(hbnb) "

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

        if not args:
            print("** class name missing **")
            return

        if len(args.split()) == 1:
            print("** instance id missing **")
            return

        className, ids = args.split()

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
            print(found_obj)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """delete an instance of the class"""

        if not args:
            print("** class name missing **")
            return

        if len(args.split()) == 1:
            print("** instance id missing **")
            return

        className, ids = args.split()

        try:
            globals()[className]
        except KeyError:
            print("** class doesn't exist **")
            return

        storage.reload()
        all_objs = storage.all()
        keys = f"{className}.{ids}"

        try:
            all_objs.pop(keys)
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

    def do_all(self, className=None):
        """print all instances created from the classNamepassed"""
        if className is None:
            print("** class name missing")

        try:
            global()[className]
        except KeyError:
            print("class doesn't exist")

        list

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
