class Node:
    def __init__(self, val=None):
        self.val = val
        self.lchild = None
        self.rchild = None


class BST:
    def __init__(self):
        self.root = None


    def insert(self, val):
        if (self.root == None):
            self.root = Node(val)
        else:
            ptr=self.root
            while ptr!=None:
                if (val < ptr.val):
                    if (ptr.lchild == None):
                        ptr.lchild = Node(val)
                        break
                    else:
                        ptr = ptr.lchild
                if (val > ptr.val):
                    if (ptr.rchild == None):
                        ptr.rchild = Node(val)
                        break
                    else:
                        ptr = ptr.rchild


    # With recursion
def inorder_recursion(curr_node,A):
        #ptr = curr_node
        if curr_node:
            inorder_recursion(curr_node.lchild,A)
            A.append(curr_node.val)
            inorder_recursion(curr_node.rchild,A)
        return A

def binary_search(f,low,high,key):
    if high>=low:
        mid=(low+high)/2
        if f[mid]==key:
            return f[mid+1:]
        elif key<f[mid]:
            return binary_search(f,low,mid-1,key)
        elif key>f[mid]:
            return binary_search(f,mid+1,high,key)
        else:
            return -1




tree=BST()
arr=[50,30,20,40,70,60,80]
for i in arr:
    tree.insert(i)
A=[]
f=inorder_recursion(tree.root,A)
low=0
high=len(f)-1
key=60
lst=binary_search(f,low,high,key)
print(lst)


#Output
#[70, 80]