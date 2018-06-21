#Creating HashTable Using Dictionary

def create_hashtable(A):
    Hash_A={}

    for i in A:
        val=(i%len(A))

        #If key present add element to list of values
        if(Hash_A.has_key(val)):
            values=Hash_A[val]
            values.append(i)
            Hash_A[val]=values
        #else new key and list added
        else:
            tmplist=[]
            tmplist.append(i)
            Hash_A[val]=tmplist
    return(Hash_A)



def check_subset(Hash_A,A,B):
    found=[]

    for i in B:
        v=(i%len(A))
        if(Hash_A.has_key(v)):
            all_vals=Hash_A[v]
            if(i in all_vals):
                found.append(1)
            else:
                found.append(0)
    return all(x==1 for x in found)













A=[5,3,8,7,10]
B=[5,7,3]

Hash_A=create_hashtable(A)
print(Hash_A)

g=check_subset(Hash_A,A,B)
if(g==1):
    print('Its a subset')