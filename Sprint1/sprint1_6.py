def order(a):
    i=1
    if a[0]<a[1]:
        while i<len(a)-1:
            if a[i]<a[i+1]:
                i=i+1
            else:
                return "not sorted"
        return "ascending"
    else:
        while i<len(a)-1:
            if a[i]>a[i+1]:
                i=i+1
            else:
                return "not sorted"
        return "descending"

a=[10,5,4]
print(order(a))
