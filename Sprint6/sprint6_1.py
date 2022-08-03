import json
from collections import OrderedDict
import os


def find(file, key):
    results = [] 

    def find_key(json_dict):
        try: 
            if type(json_dict[key]) is list:
                results.extend(json_dict[key]) 
            else:
                results.append(json_dict[key]) 
        except KeyError: 
            pass 
        return json_dict

    with open(file) as file:
        data=json.load(file, object_hook=find_key)
    
    return list(OrderedDict.fromkeys(results))


file1=os.path.dirname(__file__) + "\\files\\1.json"
file2=os.path.dirname(__file__) + "\\files\\2.json"
file3=os.path.dirname(__file__) + "\\files\\3.json"

print(find(file1, "password"))
print(find(file2, "password"))
print(find(file3, "password"))
