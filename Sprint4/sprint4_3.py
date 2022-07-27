class Employee:
    def __init__(self, full_name, **kwargs):
        setattr(self, 'name', full_name.split(" ")[0])
        setattr(self, 'lastname', full_name.split(" ")[1])
        for key in kwargs:
            setattr(self, key, kwargs[key])


john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")

print(mary.lastname)
print(richard.height)
print(giancarlo.nationality)
print(john.name)
