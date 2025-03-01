#!/usr/bin/env python
import cmd
from models.base_model import BaseModel
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """The cmd class for console manipulation it's used to work on the command line
        it inherited methods from the cmd module which shall be overriden just soon*
    """
    prompt = '(hbnb)'
    class_dict = {'BaseModel' : BaseModel}
    
    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True
    
    def do_EOF(self):
        """Exiting the console"""

        return True
    
    def do_create(self, args):
        """Create a new object as required by the command line arguments
        
        Args:
            list: list of arguments that are yet to be known, which would Idealy be 'create classname'
        """
        args = args.split()
        if len(args) < 1:
            print('** class name missing **')
            return
        else:
            class_name = args[0]
            if args[0] not in self.class_dict:
                print("** class doesn't exist **")
                return
            else:
                new_instance = self.class_dict[class_name]()
                new_instance.save()
                print(new_instance.id)
    
    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234"""
        args = args.split()
       
        if len(args) < 1:
            print('** class name missing **')
            return
        else:
            class_name = args[0]
            if args[0] not in self.class_dict:
                print("** class doesn't exist **")
                return
            else:
                if len(args) < 2:
                    print('** instance id missing **')
                else:
                    obj_id = args[1]
                    class_id = '{}.{}'.format(class_name, obj_id)
                    all_instance = storage.all()
                    result = ''
                    for key, value in all_instance.items():
                        if key != class_id:
                            result = '** no instance found **'
                        else:
                            result = value
                    print(result)

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id (save the change into the JSON file)"""
        args = args.split()
       
        if len(args) < 1:
            print('** class name missing **')
            return
        else:
            class_name = args[0]
            if args[0] not in self.class_dict:
                print("** class doesn't exist **")
                return
            else:
                if len(args) < 2:
                    print('** instance id missing **')
                else:
                    obj_id = args[1]
                    class_id = '{}.{}'.format(class_name, obj_id)
                    all_instance = storage.all()
                    result = ''
                    for key, value in all_instance.items():
                        if key != class_id:
                            result = '** no instance found **'
                        else:
                            del all_instance[key]
                            result = all_instance.save()
                    print(result)

                
            

if __name__ == '__main__':
    HBNBCommand().cmdloop()