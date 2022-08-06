import json
import pickle
from enum import Enum
from os import path


class FileType(Enum):

    JSON=1
    BYTE=2


class SerializeManager:

    def __init__(self,  filename, type):
        self.filename=filename
        self.type=type

    def __enter__(self):
        if self.type==FileType.JSON:
            self.file=open(self.filename, "w")
        elif self.type==FileType.BYTE:
            self.file=open(self.filename, 'wb')
        return self

    def __exit__(self, type, value, traceback):
        self.file.close()

    def serialize(self, object):
        if self.type==FileType.JSON:
            json.dump(object, self.file)
        elif self.type==FileType.BYTE:
            pickle.dump(object, self.file)


def serialize(object, filename, fileType):
    with SerializeManager(filename, fileType) as manager:
        manager.serialize(object)


print(isinstance(serialize.__globals__['SerializeManager'], object))
print(issubclass(FileType, Enum))

print (str(path.exists('1')))
serialize("String", "1", FileType.JSON)
print (str(path.exists('1')))

user_dict = {"name": "Hallo", "id" : 2}
serialize(user_dict, "2", FileType.BYTE)
with open("2", "rb") as file:
    print(pickle.load(file))

user_dict = {"name": "Hallo", "id" : 2}
serialize(user_dict, "2", FileType.JSON)

data = {"prop1": "value1", "prop2" : "value2"}
with SerializeManager("test_4.json", FileType.JSON) as user:
    user.serialize(data)
    