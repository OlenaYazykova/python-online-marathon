import json
from json import JSONEncoder
import os


class Student:

    def __init__(self, full_name:str, avg_rank: float, courses: list):
        self.full_name=full_name
        self.avg_rank=avg_rank
        self.courses=courses
    
    def __str__(self):
        return f'{self.full_name} ({self.avg_rank}): {self.courses}'
    
    @classmethod
    def from_json(cls, json_file):
        student=[]
        with open(json_file, 'r') as file:
            data=json.load(file)
            student.extend(data) if type(data)==list else  student.append(data)
        for item in student:
            full_name = item['full_name']
            avg_rank = item['avg_rank']
            courses = item['courses']
        return cls(full_name, avg_rank, courses)


class Group:

    def __init__(self, title: str, students: list):
        self.title=title
        self.students=students

    def __str__(self):
        return f'{self.title}: {[str(Student(**item)) for item in self.students]}'
    
    @staticmethod
    def serialize_to_json(list_of_groups, filename):
        result=[]
        for item in list_of_groups:
            res_dict={}
            res_dict["title"]=item.title
            res_dict["students"]=item.students
            result.append(res_dict)
        with open(filename, "w") as file:
            data = json.dump(result, file)

    @classmethod
    def create_group_from_file(cls, students_file):
        students_group=[]
        with open(students_file, 'r') as file:
            data=json.load(file)
            students_group.extend(data) if type(data)==list else  students_group.append(data)
        full_name=os.path.basename(students_file)
        title=os.path.splitext(full_name)[0]
        students=students_group
        return cls(title, students)


file_2020_2=os.path.dirname(__file__) + "\\files\\2020_2.json"
file_2020_01=os.path.dirname(__file__) + "\\files\\2020-01.json"
g=os.path.dirname(__file__) + "\\files\\g1.json"
print(Student.from_json(file_2020_01))

with open(file_2020_2) as read_file:
    user2 = json.load(read_file)
print([str(Student(**item)) for item in user2])

g1 = Group.create_group_from_file(file_2020_2)
g2 = Group.create_group_from_file(file_2020_01)
print(g1.title)
print(g1.students)
print(g2.title)
print(g2.students)
Group.serialize_to_json([g1, g2],g)

g1 = Group.create_group_from_file(file_2020_2)
print(g1)
	
g2 = Group.create_group_from_file(file_2020_01)
print(g2)
