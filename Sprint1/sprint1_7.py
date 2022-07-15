def Cipher_Zeroes(N):
    dict_of_zeroes={0:1, 1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:0, 8:2, 9:1}
    M=0
    for i in N:
        M+=dict_of_zeroes[int(i)]
    if M%2==0 and M>0:
        M-=1
    elif M%2==1 and M>0:
        M+=1
    if M==0:
        return 0
    M_bin=""
    while M!=0:
        M_bin+=str(M%2)
        M//=2
    return int(M_bin[::-1]) 
        
N="565" 
print(Cipher_Zeroes(N))
