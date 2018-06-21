def LIS(A):


    #Initialize two constants
    currcnt=1
    maxcnt=1
    for i in range(1,len(A)):
        if A[i]>A[i-1]:
            currcnt=currcnt+1
        else:
            if maxcnt<currcnt:
                maxcnt=currcnt
                Index=i-maxcnt
                #S=[]
            currcnt=1
    if maxcnt<currcnt:
        maxcnt=currcnt
        Index=len(A)-maxcnt

    print([A[j] for j in range(Index,Index+maxcnt)])


#Problem Statement States that the elements are present in increasing order
A=[9,10,21,22,33,41,50,60]
LIS(A)

#If not in increasing order
B=[10,21,22,9,33,60,41,50]
LIS(B)

#Output
'''[9, 10, 21, 22, 33, 41, 50, 60]
[10, 21, 22]'''
