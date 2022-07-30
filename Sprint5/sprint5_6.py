class MyError(Exception):
    def __init__(self, data):
        self.data=data
    
    def __str__(self):
        return self.data

    
def check_positive(number):
    try:
        if float(number)>0:
            return f"You input positive number: {float(number)}"
        if float(number)<0:
            raise MyError(f"You input negative number: {float(number)}. Try again.")
    except MyError as e:
        return e
    except (ValueError, TypeError):
        return "Error type: ValueError!"


print(check_positive(24))
print(check_positive(-19))
print(check_positive("38"))
print(check_positive("abc"))
print(check_positive([1, 2]))
print(check_positive({1:"a"}))
print(check_positive(-19))	
print(check_positive("45"))
print(check_positive("-235"))
