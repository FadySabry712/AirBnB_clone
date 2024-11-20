#!/usr/bin/python3
""" Deinfe The Console for the AirBnB Clone. """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Define AirBnB Holberton command interperter.
    Attributes:
        prompt: the project command prompt
    """

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Function to quit or exist the program"""
        return True

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
