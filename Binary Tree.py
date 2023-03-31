#preorder : root->left->right (1>2>4>5>3)
#inorder : left->root->right (4>2>5>1>3)
#postorder :left->right->root (4>5>2>3>1)
#A python class that represents an individual node in a Binary Tree

class Node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.val=item
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val) + "->", end='')
        inorder(root.right)       
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + "->", end='')      
def preorder(root):
    if root:
        #Traverse root
        print(str(root.val) + "->", end='')
        #Traverse left
        preorder(root.left)
        #Traverse right
        preorder(root.right)    
root=Node(1)#1000
root.left=Node(2)#2000
root.right=Node(3)#3000
root.left.left=Node(4)#4000
root.left.right=Node(5)#5000
print("Inorder traversal")
inorder(root)
print("\nPreorder traversal")
preorder(root)
print("\nPostorder traversal")
postorder(root)
