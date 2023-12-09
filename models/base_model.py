#!/usr/bin/python3
"""Base model defining common attributes/methods for other classes"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base class inherited by other classes"""

    def _init_(self, *args, **kwargs):
        """Initializes instance attributes"""

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self._dict_["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self._dict_["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self._dict_[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def _str_(self):
        """Official string representation"""

        return "[{}] ({}) {}".\
            format(type(self)._name, self.id, self.__dict_)

    def save(self):
        """Updates the public instance attribute updated_at"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of _dict_"""

        my_dict = self._dict_.copy()
        my_dict["_class"] = type(self).__name_
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
