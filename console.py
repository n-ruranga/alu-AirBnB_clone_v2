#!/usr/bin/python3
"""
AirBnB Clone Project - Console
Command interpreter entry point
"""
import cmd
import shlex
import ast
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for AirBnB clone project
    """

    prompt = "(hbnb) "
    className = {'BaseModel': BaseModel,
                 'User': User,
                 'State': State,
                 'City': City,
                 'Amenity': Amenity,
                 'Place': Place,
                 'Review': Review}

    def do_create(self, arg):
        """Create an instance with optional parameters: create Class key=value ...

        Strings must be in double quotes; underscores are converted to spaces.
        Floats contain a dot, integers contain only digits.
        Invalid params are skipped.
        """
        if not arg:
            print("** class name missing **")
            return
        parts = shlex.split(arg)
        class_name = parts[0]
        if class_name not in HBNBCommand.className.keys():
            print("** class doesn't exist **")
            return
        obj = HBNBCommand.className[class_name]()

        def cast_value(val):
            # Try int
            try:
                if val.isdigit():
                    return int(val)
            except AttributeError:
                pass
            # Try float
            try:
                if val.replace('.', '', 1).isdigit() and val.count('.') == 1:
                    return float(val)
            except AttributeError:
                pass
            # String: replace underscores with spaces
            if isinstance(val, str):
                return val.replace('_', ' ')
            return val

        for token in parts[1:]:
            if '=' not in token:
                continue
            key, value = token.split('=', 1)
            if not key:
                continue
            # If quoted string, keep inner content and unescape quotes
            if len(value) >= 2 and value[0] == '"' and value[-1] == '"':
                inner = value[1:-1].replace('\\"', '"')
                setattr(obj, key, inner.replace('_', ' '))
                continue
            # Otherwise attempt numeric cast or underscore-space conversion
            casted = cast_value(value)
            try:
                setattr(obj, key, casted)
            except Exception:
                continue

        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Show command to print the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        if args[0] not in HBNBCommand.className.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0]+'.'+args[1] not in models.storage\
                                              ._FileStorage__objects.keys():
            print("** no instance found **")
        else:
            print(models.storage._FileStorage__objects[args[0]+'.'+args[1]])

    def do_destroy(self, arg):
        """Destroy command to delete an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        if args[0] not in HBNBCommand.className.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0]+'.'+args[1] not in models.storage\
                                              ._FileStorage__objects.keys():
            print("** no instance found **")
        else:
            del models.storage._FileStorage__objects[args[0]+'.'+args[1]]
            models.storage.save()

    def do_all(self, arg):
        """All command to print all instances of a/all class/es"""
        if not arg:
            list_objs = []
            for key, obj in models.storage._FileStorage__objects.items():
                list_objs.append(str(obj))
            if len(list_objs) > 0:
                print(list_objs)
        else:
            if arg not in HBNBCommand.className.keys():
                print("** class doesn't exist **")
            else:
                list_objs = []
                for key, obj in models.storage._FileStorage__objects.items():
                    if arg == key.split('.')[0]:
                        list_objs.append(str(obj))
                if len(list_objs) > 0:
                    print(list_objs)

    def do_update(self, arg):
        """Update command to add or update attributes"""
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        if args[0] not in HBNBCommand.className.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0]+'.'+args[1] not in models.storage\
                                              ._FileStorage__objects.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj = models.storage._FileStorage__objects[args[0]+'.'+args[1]]
            if args[2] in obj.__dict__.keys():
                try:
                    if args[3].isdigit():
                        args[3] = int(args[3])
                    elif args[3].replace('.', '', 1).isdigit():
                        args[3] = float(args[3])
                except AttributeError:
                    pass
                setattr(obj, args[2], args[3])
            else:
                try:
                    if args[3].isdigit():
                        args[3] = int(args[3])
                    elif args[3].replace('.', '', 1).isdigit():
                        args[3] = float(args[3])
                except AttributeError:
                    pass
                setattr(obj, args[2], args[3])
            HBNBCommand.className[args[0]].save(obj)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
