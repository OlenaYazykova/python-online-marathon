def studying_hours(a):
    subarray=[a[0]]
    max_subbarray=0
    length_subbarray=0
    for i in range(0,len(a)-1):
        if a[i]<=a[i+1]:
            subarray.append(a[i+1])
            length_subbarray=len(subarray)
        else:
            if max_subbarray<length_subbarray:
                max_subbarray=length_subbarray
            subarray.clear()
            subarray.append(a[i+1])
    if max_subbarray>=length_subbarray:
        return max_subbarray
    else:
        return length_subbarray


a=[2,2,1,3,4,1]
print(studying_hours(a))
