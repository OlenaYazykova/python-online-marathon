def double_string(data):
    counter=0
    for i in data:
        if any(i+j in data for j in data):
            counter+=1
    return counter


data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qweraaaa'] #4
print(double_string(data))
