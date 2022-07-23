def logger(func):
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        arguments=f"Executing of function {func.__name__} with arguments "
        for i in args:
            arguments+=f'{str(i)}, '
        for j in kwargs:
            arguments+=f'{kwargs[j]}, '
        arguments=arguments[:-2]
        arguments+='...'
        print(arguments)
        return return_value
    return wrapper


@logger
def concat(*args,**kwargs):
    my_str=""
    for i in args:
        my_str+=str(i)
    for j in kwargs:
        my_str+=str(kwargs[j])
    return my_str


@logger
def sum(a,b):
    return a+b

 
@logger
def print_arg(arg):
    print(arg)


print(concat(first='hello',second=3))	
print(concat(1))
print(concat('first string', second = 2, third = 'second string'))
print(concat('first string', {'first kwarg' :0, 'second kwarg': 'second kwarg'}))
print(sum(2,3))
dict_args={'first kwarg' :0, 'second kwarg': 'second kwarg'}
concat(**dict_args)	
print_arg(2)
