def isPalindrome(str):
    my_set=set(str)
    number_of_char=[]
    for i in my_set:
        number_of_char.append(str.count(i))
    even_number=0
    for i in number_of_char:
        if i%2==0:
            even_number+=1
    if  even_number==len(my_set) or even_number==len(my_set)-1:
        return True
    else:
        return False


print(isPalindrome("trueistrue"))
