#import sys
#infile=sys.argv[1]

#with open(infile,'r') as r1:

          #lines=[int(i) for i in r1]
          

#print(lines)



def bubble_sort(arr):
    for j in range(0,len(arr)):
        for i in range(0,len(arr)-1-j):
            if (arr[i]>arr[i+1]):
                arr=swap(arr,i,i+1)
    return arr


def swap(arr,a,b):
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp
    return arr
            
#arr=bubble_sort(lines)
#print(arr)

def insertion_sort(arr):
    for i in range(1,len(arr)):
        hold=arr[i]
        j=i-1
        while(j>=0 and hold<arr[j]):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=hold
    return arr


lines=[7,5,10,14,3]
arr=bubble_sort(lines)
print(arr)

lines1=[7,85,4,12]
arr1=insertion_sort(lines1)
print(arr1)