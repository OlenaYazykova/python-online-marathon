import json
import jsonschema
from jsonschema import validate
import csv
import os


class  InvalidInstanceError(Exception): 

    def __init__(self, data):
        self.data=data

    def __str__(self):
        return self.data

class  DepartmentName(Exception): 

    def __init__(self, data):
        self.data=data

    def __str__(self):
        return self.data

user_schema = { 
                "type" : "object", 
                "properties" : {
                    "id" : {"type" : "number"}, 
                    "name" : {"type" : "string"},
                    "department_id" : {"type" : "number"}
                    },
                    "required": ["id","name", "department_id"]
            }

department_schema = { 
                "type" : "object", 
                "properties" : {
                    "id" : {"type" : "number"}, 
                    "name" : {"type" : "string"},
                    },
                    "required": ["id","name"]
            }

def validate_json(data, schema):
    if len((schema['required']))==2:
        inst="department"
    else:
        inst="user"

    for item in data:
        try:
            validate(item, schema)
        except jsonschema.exceptions.ValidationError:
                raise InvalidInstanceError(f"Error in {inst} schema")

def write_csv(csv_file, result):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file, delimiter= ',')
        writer.writerow(['name', 'department'])
        for item in result:
            writer.writerow(item)
    return csv_file

def user_with_department(csv_file, user_json, department_json):
    result=[]

    with open(user_json, 'r') as file:
        user=json.load(file)
    validate_json(user, user_schema)

    
    with open(department_json, 'r') as file:
        department=json.load(file)
    validate_json(department, department_schema)

    for i in user:
        lst=[]
        for j in department:
            if i['department_id']==j['id']:
                lst.append(i['name'])
                lst.append(j['name'])
                result.append(lst)
        if lst==[]:
            raise DepartmentName(f"Department with id {i['department_id']} doesn't exists")
    
    write_csv(csv_file, result)
    
    return csv_file


user_json=os.path.dirname(__file__) + "\\files\\user.json"
department_json=os.path.dirname(__file__) + "\\files\\department.json"
csv_file=os.path.dirname(__file__) + "\\files\\user_department.csv"

print(user_with_department(csv_file, user_json, department_json))
	
try:
    user_with_department(csv_file, user_json, department_json)
except InvalidInstanceError as e:
    print(str(e))

try:
  user_with_department(csv_file, user_json, department_json)
except DepartmentName as e:
    print(str(e))
    