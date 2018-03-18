def left(i):
    return(2*i+1)
def right(i):
    return(2*i+2)


def parent(i):
    parent=((i)/2)
    return(parent)


def swap(A,a,b):
    A[a],A[b]=A[b],A[a]
    return(A)

def down(A,i):

    l=left(i)
    r=right(i)
    max_element=i
    #Checking if the left node is larger than root
    if(l<len(A)):
        if(A[l]>A[max_element]):
            max_element=l

    #Checking if the right node is larger than root
    if(r<len(A)):
        if(A[r]>A[max_element]):
            max_element=r

    #Checking the heap property with the root node
    if(max_element!=i):
        A=swap(A,max_element,i)
        A=down(A,max_element)

    if (l < len(A) and r < len(A)):
        if (A[l] < A[r]):
         A = swap(A, l, r)

    return(A)


def build_max_heap(A):
    A_heapsize= len(A)
    for i in range(parent(A_heapsize-1),-1,-1):
        A=down(A,i)
    return(A)

def sort_heap(A):
    heap_size=len(A)-1
    tmp_b=[]
    for i in range(heap_size,-1,-1):
        A=swap(A,0,i)
        tmp_b.append(A[i])
        del A[i]
        A=build_max_heap(A)
    tmp_b.reverse()
    return(tmp_b)


#A=[15,13,9,5,12,8,7,4,0,6,2,1]

#A=[4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
#A=[4,10,3,5,1]
A=[35,33,42,10,14,19,27,44,26,31]
A=build_max_heap(A)

#Sort the array
tmp_b=sort_heap(A)
#tmp_a=[]
#tmp_a=tmp_b.reverse()
print("The Final sorted Heap",tmp_b)