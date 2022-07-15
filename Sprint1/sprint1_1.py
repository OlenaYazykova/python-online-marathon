def kthTerm(n, k):
    seq1=[1]
    p=1
    while len(seq1)<=100:
        seq2=[]
        seq2.append(n**p)
        for i in range(0,len(seq1)):
            seq2.append(n**p+seq1[i])
        seq1.extend(seq2)
        p=p+1
    #print(seq1)
    return seq1[k-1]

print(kthTerm(30,100))
