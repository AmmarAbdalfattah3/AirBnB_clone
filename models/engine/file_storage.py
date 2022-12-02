#!/user/bin/python3
"""File_storage module"""
import json



class FileStorage:
    """
       class FileStorage that serializes instances to a
       JSON file and deserializes JSON file to instances:
    """
    __file_path = "./file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects
    def new(self, obj):
        """sets in __objects the obj
           with key <obj class name>.id
        """
        FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj
    def save(self):
        """serializes __objects to the
           JSON file (path: __file_path)
        """
        last_dict = {}
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as json_file:
            for key, value in FileStorage.__objects.items():
                last_dict[key] = value.to_dict()

            json.dump(last_dict, json_file)

    def reload(self):
        """deserializes the JSON file to __objects
           (only if the JSON file (__file_path) exists ; otherwise,
           do nothing. If the file doesn’t exist,
           no exception should be raised)
        """
        from models.base_model import BaseModel
        from models.state import State
        from models.review import Review
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.city import City

        try:
            with open(FileStorage.__file_path, encoding="UTF-8") as json_file:
                restored_dict = json.load(json_file)
                for value in restored_dict.values():
                    self.new(eval(value["__class__"])(**value))
        except FileNotFoundError:
            return
