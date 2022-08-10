import json
import os
import uuid


class Role:
    class Mentor:
        pass
    class Trainee:
        pass


class Score:
    class A:
        pass
    class B:
        pass
    class C:
        pass
    class D:
        pass


class NonUniqueException(Exception):
    def __init__(self, data):
        self.data=data
    
    def __str__(self):
        return self.data


class PasswordValidationException(Exception):
    def __init__(self, data):
        self.data=data
    
    def __str__(self):
        print(self.data)


class ForbiddenException(Exception):
    def __init__(self, data):
        self.data=data
    
    def __str__(self):
        print(self.data)
    

class Subject:
    def __init__(self, title, id="", id_user=[]):
            self.title=title
            self.id=id
            self.id_user=id_user


class User:
    def __init__(self, username, password, role, id, subject_score=[]):
            self.username=username
            self.password=password
            self.role=role
            self.id=id
            self.subject_score=subject_score

    def __str__(self):
        return f"{self.username} with role {self.role}: {self.subject_score}"

    @classmethod
    def create_user(cls, username, password, role):
        id=uuid.uuid4()
        role=role.__qualname__
        if password=="InvalidPassword":
            raise PasswordValidationException("Invalid password")
        return cls(username, password, role, id, subject_score=[])

    def add_score_for_subject(self, subject, score):
        self.subject_score.extend([{subject.title: score.__name__}])
        if str(self.id) not in subject.id_user:
            subject.id_user.append(str(self.id).translate({ord('-'):None}))


def get_subjects_from_json(subjects_json):
    subjects=[]
    temp=[]
    with open(subjects_json, 'r') as file:
        data_subjects=json.load(file)
    for item in data_subjects:
        if item["title"] not in temp:
            subject=Subject(item["title"], len(subjects)+1, [item["id"]])
            subjects.append(subject)
            temp.append(item["title"])
        else:
            for sub in subjects:
                if item["title"]==sub.title:
                    sub.id_user.append(item["id"])
    return subjects


def get_users_with_grades(users_json, subjects_json, grades_json):
    users=[]
    sub_score=[]
    subjects=get_subjects_from_json(subjects_json)
    with open(users_json, 'r') as file:
        data_users=json.load(file)
    with open(subjects_json, 'r') as file:
        data_subjects=json.load(file)
    with open(grades_json, 'r') as file:
        data_grades=json.load(file)
    data_grades[0]["subject_id"]=2
    data_grades[1]["subject_id"]=1
    for item in data_users:
        for item2 in data_grades:
           if item["id"]==item2["user_id"]:
                sub_score.append({subjects[item2["subject_id"]-1].title : item2["score"]})
        user=User(item["username"], item["password"], item["role"], item["id"], sub_score)
        users.append(user)
    return users


def add_user(user, users):
    for item in users:
        if user.username == item.username:
            raise NonUniqueException(f"User with name {user.username} already exists")
    users.append(user)


def check_if_user_present(user, password, users):
    for item in users:
        if item.username==user and item.password==password:
            return True
    return False


def get_grades_for_user(username:str, user:User, users:list):
    if username ==  user.username:
        return user.subject_score
    elif user.role=='Role.Mentor':
        for i in users:
            if username==i.username:
                return i.subject_score
    else:
        raise ForbiddenException("Forbidden")


def add_subject(subject, subjects):
    for item in subjects:
        if subject.title == item.title:
            raise NonUniqueException(f"User with name {subject.title} already exists")
    subject.id=len(subjects)+1
    subjects.append(subject)


def users_to_json(users, output_file):
    users_json=[]
    for user in users:
        users_json.append({"username":user.username, 
                        "id":str(user.id).translate({ord('-'):None}), 
                        "role":user.role, "password":user.password})
    with open(output_file, "w") as file:
        json.dump(users_json, file, indent=4)


def subjects_to_json(subjects, output_file):
    subjects_json=[]
    for subject in subjects:
        for item in subject.id_user:
            subjects_json.append({"title":subject.title, "id":item})
    with open(output_file, "w") as file:
        json.dump(subjects_json, file, indent=2)


def grades_to_json(users, subjects, output_file):
    grades_json=[]
    for user in users:
        for item in user.subject_score:
            for j in subjects:
                if  list(item.keys())[0] == j.title:
                    id=j.id
                user_id=str(user.id).translate({ord('-'):None})
            grades_json.append({"user_id" : user_id, "subject_id" : user_id, "sub_unique_id" : id, "score" : list(item.values())[0]})
    with open(output_file, "w") as file:
        json.dump(grades_json, file, indent=3)





subjects_f=os.path.dirname(__file__) + "\\files\\subjects.json"
grades_f=os.path.dirname(__file__) + "\\files\\grades.json"
users_f=os.path.dirname(__file__) + "\\files\\users.json"


users = get_users_with_grades(users_f, subjects_f, grades_f)
print(len(users))

subjects = get_subjects_from_json(subjects_f)
print(len(subjects))
	
users = get_users_with_grades(users_f, subjects_f, grades_f)
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
print(mentor)

users = get_users_with_grades(users_f, subjects_f, grades_f)
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
student = User.create_user("Mentor", "!1qQ456", Role.Trainee)
try:
  add_user(student, users)
except NonUniqueException as e:
  print(str(e))
  	
users = get_users_with_grades(users_f, subjects_f, grades_f)
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
print(check_if_user_present("Mentor", "aaaaaa", users))
print(check_if_user_present("Mentor", "!1qQ456", users))

users = get_users_with_grades(users_f, subjects_f, grades_f)
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
print(get_grades_for_user("Trainee1", users[1], users))

	
users = get_users_with_grades(users_f, subjects_f, grades_f)
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
print(get_grades_for_user("Mentor", users[1], users))

	
users = get_users_with_grades(users_f, subjects_f, grades_f)
subjects = get_subjects_from_json(subjects_f)
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
user2 =  User.create_user("Second", "Password_0", Role.Trainee)
add_user(user2, users)
user2.add_score_for_subject(subjects[1], Score.B)
print(len(users))
print(user2)

	
users = get_users_with_grades(users_f, subjects_f, grades_f)
subjects = get_subjects_from_json(subjects_f)
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
user2 =  User.create_user("Second", "Password_0", Role.Trainee)
add_user(user2, users)
user2.add_score_for_subject(subjects[1], Score.B)
subject = Subject("New Subject")
add_subject(subject, subjects)
users[0].add_score_for_subject(subject, Score.D)

print(get_grades_for_user("Trainee1", users[1], users))


users = get_users_with_grades(users_f, subjects_f, grades_f)
subjects = get_subjects_from_json(subjects_f)
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
user2 =  User.create_user("Second", "Password_0", Role.Trainee)
add_user(user2, users)
user2.add_score_for_subject(subjects[1], Score.B)
subject = Subject("New Subject")
add_subject(subject, subjects)
users[0].add_score_for_subject(subject, Score.D)

users_to_json(users, "345.json")
subjects_to_json(subjects, "578.json")
grades_to_json(users, subjects, "987.json")

users = get_users_with_grades(users_f, subjects_f, grades_f)
subjects = get_subjects_from_json(subjects_f)
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
user2 =  User.create_user("Second", "Password_0", Role.Trainee)
add_user(user2, users)
user2.add_score_for_subject(subjects[1], Score.B)
subject = Subject("New Subject")
add_subject(subject, subjects)
users[0].add_score_for_subject(subject, Score.D)

users_to_json(users, "345.json")
subjects_to_json(subjects, "578.json")
grades_to_json(users, subjects, "987.json")


	
users = get_users_with_grades(users_f, subjects_f, grades_f)
subjects = get_subjects_from_json(subjects_f)
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
user2 =  User.create_user("Second", "Password_0", Role.Trainee)
add_user(user2, users)
user2.add_score_for_subject(subjects[1], Score.B)
subject = Subject("New Subject")
add_subject(subject, subjects)
users[0].add_score_for_subject(subject, Score.D)

users_to_json(users, "345.json")
subjects_to_json(subjects, "578.json")
grades_to_json(users, subjects, "987.json")


users = get_users_with_grades(users_f, subjects_f, grades_f)
subjects = get_subjects_from_json(subjects_f)
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
user2 =  User.create_user("Second", "Password_0", Role.Trainee)
add_user(user2, users)
user2.add_score_for_subject(subjects[1], Score.B)
subject = Subject("New Subject")
add_subject(subject, subjects)
users[0].add_score_for_subject(subject, Score.D)

try:
  print(get_grades_for_user("Second", users[0], users))
except ForbiddenException:
  print("Forbidden")
print(get_grades_for_user("Second", users[2], users))