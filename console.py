#!/usr/bin/python3
"""console module"""

import cmd
import sys
import shlex
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.__init__ import storage

model_classes = [
    "BaseModel",
    "User",
    "City",
    "Place",
    "State",
    "Amenity",
    "Review"
]

def class_name(args):
    if len(args) == 0:
        print("** class name missing **")
        return
    list_args = shlex.split(args)
    if list_args[0] not in model_classes:
        print("** class doesn't exist **")
        return
    return list_args


class HBNBCommand(cmd.Cmd):
    """ the module that contains the entry
        point of the command interpreter
    """
    prompt = "(hbnb) "
    def do_quit(self, args):
        """Quit command to exit the program"""
        return True
    def do_EOF(self, args):
        """exit the program"""
        print("")
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def default(self, args):
        """ Default the function handles special command syntax"""
        commands = {"all": self.do_all,
                  "update": self.do_update,
                  "show": self.do_show,
                  "count": self.do_count,
                  "destroy": self.do_destroy}

        cleaner = (args.replace("(", ".").replace(")", ".")
                    .replace('"', "").replace(",", "").split("."))

        try:
            n_args = cleaner[0] + " " + cleaner[2]
            print(n_args)
            command = commands[cleaner[1]]
            command(n_args)
        except:
            print("*** Unknown syntax:", args[0])


    def do_create(self, args):
        """Creates a new instance of BaseModel,
           saves it (to the JSON file) and prints the id.
        """

        list_args = class_name(args)
        if not list_args:
            return
        model = eval(list_args[0])()
        model.save()
        print(model.id)



    def do_show(self, args):
        """Prints the string representation of an instance
           based on the class name and id
        """
        list_args = class_name(args)
        if not list_args:
            return
        if len(list_args) == 1:
            print("** instance id missing **")
            return
        reloaded_dict = storage.all()
        key = list_args[0] + "." + list_args[1]
        try:
            obj = reloaded_dict[key]
            print(obj)
        except KeyError:
            print("** no instance found **")
    def do_destroy(self, args):
        """Deletes an instance based on the class name
           and id (save the change into the JSON file).
        """
        list_args = class_name(args)
        if not list_args:
            return
        if len(list_args) == 1:
            print("** instance id missing **")
            return
        reloaded_dict = storage.all()
        key = list_args[0] + "." + list_args[1]
        try:
            del reloaded_dict[key]
            storage.save()

        except KeyError:
            print("** no instance found **")
    def do_all(self, args):
        rel_dict = storage.all()
        if not args:
            print([str(obj) for obj in rel_dict.values()])
        if args:
            list_args = shlex.split(args)
            if list_args[0] not in model_classes:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in rel_dict.values()
                       if list_args[0] in str(obj)])
    def do_update(self, args):
        """Updates an instance based on the class name and id by
           adding or updating attribute (save the change into the JSON file).
        """
        reloaded_dict = storage.all()
        list_args = class_name(args)
        if not list_args:
            return
        if len(list_args) == 1:
            print("** instance id missing **")
            return
        elif len(list_args) == 2:
            print("** attribute name missing **")
            return
        elif len(list_args) == 3:
            print("** value missing **")
            return

        key = list_args[0] + "." + list_args[1]

        try:
            obj= reloaded_dict[key]
            try:
                attr_type = type(getattr(obj, list_args[2]))
                list_args[3] = eval(attr_type.__name__)(list_args[3])
            except AttributeError:
                pass
            setattr(obj, list_args[2], list_args[3])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_count(self, args):
        """etrieve the number of instances of
           a class: <class name>.count().
        """
        counter = 0
        reloaded_dict = storage.all()
        list_args = class_name(args)
        if not list_args:
            return
        
        for key, value in reloaded_dict.items():
            if list_args[0] == type(value).__name__:
                counter += 1
        print(counter)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
