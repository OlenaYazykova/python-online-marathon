def create(arg1):
    return lambda arg2: arg2==arg1


tom = create("pass_for_Tom") 
print(tom("pass_for_Tom"))
print(tom("pass_for_tom"))
