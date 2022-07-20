def findPermutation(n, p, q):
    r=[]
    for i in q:
        r.append(p.index(i)+1)
    return r


n=3
p=[3,1,2]
q=[2,1,3]
print(findPermutation(n, p, q))
