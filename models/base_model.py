#!/usr/bin/python3
"""module for basemodel"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """ BaseModel class that defines all common
        attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """instantiates the created instance"""
        if kwargs:
            if "__class__" in kwargs.keys():
		del kwargs["__class__"]

            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    kwargs[key] = datetime.fromisoformat(value)

            self.__dict__ = kwargs

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """ updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all
           keys/values of __dict__ of the instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__

        for key, value in dict_copy.items():
            if key in ("created_at", "updated_at"):
                dict_copy[key] = value.isoformat()

        return dict_copy

    def __str__(self):
        return f"{self.__class__.__name__} {self.id} {self.__dict__}"
