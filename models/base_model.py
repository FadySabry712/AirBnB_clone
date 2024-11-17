#!/usr/bin/python3
''' base model class defination '''
import models
from uuid import uuid4
from datetime import datetime

class BaseModel
''' this is a base module to generate a unique id using UUID '''

    def __init__(self, *args, **kwargs):
        """ a new BaseModel instance0
        Args:
            *args (any)
            **kwargs (dict): Key/value pairs.
        """
        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_form)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """ keep updated_at with the current date-time"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance."""

        current_dict = self.__dict__.copy()
        current_dict["created_at"] = self.created_at.isoformat()
        current_dict["updated_at"] = self.updated_at.isoformat()
        cureent_dict["__class__"] = self.__class__.__name__
        return current_dict

    def __str__(self):
        """Return the string represntaion of the Model Instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
