#!/usr/bin/env python
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage




class HBNBCommand(cmd.Cmd):
    """The cmd class for console manipulation it's used to work on the command line
        it inherited methods from the cmd module which shall be overriden just soon*
    """
    prompt = '(hbnb)'
    class_dict = {'BaseModel' : BaseModel, 'User' : User, 'Place' : Place, 'State' : \
                  State, 'City' : City, 'Amenity' : Amenity, 'Review' : Review}
    
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
                    if class_id not in all_instance:
                        print("** No instance found")
                    else:
                        print(all_instance[class_id])

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id (save the change into the JSON file)"""
        args = args.split()
       
        if len(args) < 1:
            print('** class name missing **')
            return
        else:
            class_name = args[0]
            if class_name not in self.class_dict:
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
                    if class_id not in all_instance:
                        print("** no instance found **")
                        return
                    
                    del all_instance[class_id]
                    storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name."""
        args = args.split()
        
        # When the argument is just all and nothing more 
        if len(args) == 0:
            print(storage.all()) # Just prints all the objects already created
        else:
            instances = storage.all()
            new = {}
            for key, value in instances.items():
                if args[0] == key.split('.')[0]:
                    new[key] = value
            if new:
                print(new)
            else:
                print("** class doesn't exist **")
            
                    
    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = args.split()
        num_args = len(args)
        instances = storage.all()

        if num_args < 1:
            print("** class name missing **")
            return
        if args[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        if num_args == 1:
            print("** instance id missing **")
            return

        class_id = args[0] + '.' + args[1]

        if class_id not in instances:
            print("** no instance found **")
            return
        if num_args == 2:
            print("** attribute name missing **")
            return
        if num_args == 3:
            print("** value missing **")
            return
        
        instance = instances[class_id]
        attr = args[2]
        val = args[3]

        setattr(instance, attr, val)

        instance.save()
        

            

if __name__ == '__main__':
    HBNBCommand().cmdloop()