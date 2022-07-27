class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname=firstname
        self.lastname=lastname
        self.salary=salary

    @classmethod
    def from_string(cls,str_attr):
        list_attr=str_attr.split("-")
        firstname=list_attr[0]
        lastname=list_attr[1]
        salary=int(list_attr[2])
        return cls(firstname, lastname, salary)


emp1=Employee("Mary", "Sue", 60000)
print(emp1.firstname)
print(emp1.lastname)
print(emp1.salary)
print(isinstance(emp1.salary, int))


str_attr="Jhon-Smith-55000"
emp2=Employee.from_string(str_attr)
print(emp2.firstname)
print(emp2.lastname)
print(emp2.salary)
print(isinstance(emp2.salary, int))
