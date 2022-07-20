def morse_number(n):
    res=""
    for i in range(len(n)):
        if int(n[i])<=5:
            res+="."*int(n[i])+'-'*(5-int(n[i]))
        elif 5<int(n[i])<=9:
            res+="-"*(int(n[i])-5)+"."*(10-int(n[i]))
        if i<len(n)-1:
            res+=" "
    return res


n="295"
print(morse_number(n))
