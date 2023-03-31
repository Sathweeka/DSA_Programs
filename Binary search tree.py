'''
what is binary search tree?
Binary search tree is a node-based binary tree data structure which has
following properties:
left should be less than root
right should be greater than root
deletion operation
there are 3 cases for deletion
case 1: if it is a leaf node 4 6
'''
class Node:
    def __init__(self, key):
        self.key=key
        self.left=None
        self.right=None
        
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key) + "->", end='')
        inorder(root.right)
def insert(node, key):#node=1000, key=6
    if node is None:
        return Node(key)#3000
    if key < node.key:
        node.left = insert(node.left, key)#None, 1
    else:
        node.right = insert(node.right, key)
    return node
def minValueNode(node):
    current = node#6000
    #find the leftmost leaf
    while(current.left is not None):
        current = current.left#current=4000
    return current
def deleteNode(root, key):#8000 3000 4 6
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right#temp = None
            root = None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=minValueNode(root.right)
        root.key=temp.key
        root.right=deleteNode(root.right,temp.key)
    return root  
        
    
root = None
root = insert(root, 8)#1000,8
root = insert(root, 3)#1000,3
root = insert(root, 1)#1000,1
root = insert(root, 6)#1000,6
root = insert(root, 7)#1000,7
root = insert(root, 10)#1000,10
root = insert(root, 14)#1000,14
root = insert(root, 4)#1000,4
print("Inorder traversal: ", end=' ')
inorder(root)
print("\nDelete 6")
root = deleteNode(root, 6)
print("Inorder traversal: ", end=' ')
inorder(root)
