class ToSmallNumberGroupError(Exception): 
    def __init__(self, data):
        self.data=data

    def __str__(self):
        return self.data


def check_number_group(number):
    try:
        if float(number)>10:
            return f"Number of your group {number} is valid"    
        if float(number)<=10:
            raise ToSmallNumberGroupError("We obtain error:Number of your group can't be less than 10")
    except ToSmallNumberGroupError as e:
        return e
    except (ValueError, TypeError):
        return 'You entered incorrect data. Please try again.'


print(check_number_group(75))
print(check_number_group("96"))
print(check_number_group("abc"))
print(check_number_group(0.8))
print(check_number_group(-9))
print(check_number_group([1, 2]))
