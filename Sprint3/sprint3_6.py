import random


def randomWord(list):
    if list==[]:
        yield None
    copy_list=list[:]
    while True:
        new_list=[]
        for i in range(len(copy_list)):
            word=copy_list.pop(random.randrange(len(copy_list)))
            new_list.append(word)
            if len(copy_list)==0:
                copy_list=new_list
                new_list=[]
            yield word


list = ['book', 'apple', 'word']
books = randomWord(list)
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))


import collections

double_list = ["word1", "Biggg word", "last word"]
actual_list = []
random_element = randomWord(double_list)
for _ in range(len(double_list)*2):
  actual_list.append(next(random_element))
print(collections.Counter(set(actual_list))==collections.Counter(set(double_list*2)))
