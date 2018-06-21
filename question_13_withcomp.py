

#perform merge sort
def merge(left,right):
    i=0
    j=0
    l2=[]
    while i<len(left) and j<len(right):
        if (left[i]<right[j]):
            l2.append(left[i])
            i=i+1
        else:
            l2.append(right[j])
            j=j+1
    l2=l2+left[i:]
    l2=l2+right[j:]
    return(l2)

def merge_sort(lst):
    if(len(lst)<=1):
        return lst
    mid= int(len(lst)/2)
    left=merge_sort(lst[:mid])
    right=merge_sort(lst[mid:])
    return(merge(left,right))



#perform binary search


def perform_search(high,low,i,lst):
    if(low<=high):
        mid=low+(high)/2
        if lst[mid]==i:
            return True
        elif lst[mid]>i:
            return perform_search(mid-1,low,i,lst)
        else:
            return perform_search(high,mid+1,i,lst)
    return False


def binary_search(lst,B):
    high=len(lst)-1
    low=0
    #found=[0 for x in range(0,len(B))]
    found=[]
    for i in B:
        print(i)
        flag=perform_search(high,low,i,lst)
        if flag==True:
            found.append(1)
        else:
            found.append(0)
            #flag=False
    if(all(j==1 for j in found)):
        print(found)
        print('The List B is subset of List A')
    else:
        print(found)
        print('The List B is not a subset of List A')





A=[5,3,8,7,10]
B=[5,7,3]

#Merge sort of first array

lst=merge_sort(A)
print(lst)
binary_search(lst,B)

#output
'''[3, 5, 7, 8, 10]
5
7
3
[1, 1, 1]
The List B is subset of List A'''