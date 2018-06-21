def merge(left,right):
    i=0
    j=0
    l2=[]
    while i<len(left) and j<len(right):
        if (left[i]<right[j]):
            l2.append(left[i])
            i=i+1
        else:
            if(left[i]==right[j]):
                j=j+1
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

A=[10,3,5,4]
print(merge_sort(A))
