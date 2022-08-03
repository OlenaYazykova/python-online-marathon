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
        return self

    def __exit__(self, type, value, traceback):
        pass

    def serialize(self, object):
        self.object=object
        if self.type==FileType.JSON:
            with open(self.filename, "w") as file:
                data = json.dump(self.object, file)
        elif self.type==FileType.BYTE:
            with open(self.filename, 'wb') as file:
                pickle.dump(self.object, file)


def serialize(object, filename, fileType):
    with SerializeManager(filename, fileType) as manager:
        manager.serialize(object)


print (str(path.exists('1')))
serialize("String", "1", FileType.JSON)
print (str(path.exists('1')))
