def day_of_week(day):
    day_of_week={1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
    try:
        if type(day) is float:
            raise KeyError
        return day_of_week[int(day)]
    except KeyError:
        return "There is no such day of the week! Please try again."
    except (ValueError, TypeError):
        return "You did not enter a number! Please try again."


print(day_of_week(2))
print(day_of_week(11))
print(day_of_week("3"))
print(day_of_week("Monday"))
print(day_of_week([1, 2]))
print(day_of_week(2.8))
