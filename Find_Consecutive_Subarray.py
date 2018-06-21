#Finding the consecutive subarray



def find_subarray(a,N):
    sum=0
    index=0
    for i in range(0,len(a)):

        if(i<len(a)):
            sum=sum+a[i]
        while(sum>N):
            if(index<i-1):
                sum=sum-a[index]
                index=index+1
        if(sum==N):
            return 1









a=[5,3,8,7,10]
N=15
find=find_subarray(a,N)
if(find==1):
    print('found subarray')

#Output
#found subarray