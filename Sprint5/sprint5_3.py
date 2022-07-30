def check_odd_even(number):
    try:
        if number%2==0:
            return 'Entered number is even'
        else:
            return "Entered number is odd"
    except TypeError:
        return "You entered not a number."


number=2.8
print(check_odd_even(number))
print(check_odd_even (24))
print(check_odd_even (19))
