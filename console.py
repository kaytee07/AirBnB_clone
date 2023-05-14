#!/usr/bin/python3
"""command interpreter representing user interface for airbnb"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
    this class is going to be the command line interface where
    users can interact with the hbnb clone
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """Override emptyline method to do nothing."""
        pass

    def do_quit(self, *args):
        """This is to exit the program"""
        return True

    def do_EOF(self, line):
        """This is also to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
