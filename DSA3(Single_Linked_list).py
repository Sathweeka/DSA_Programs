#Single Liked list
'''
Traversing a Linked List
create a node in node address is stored.
linked listis a collection of nodes.
first node is called head.every node has two parts i.e., data and address of
next node.
single likedlist -traverse only in one direction i.e., right to left
instertion or deletion can be done from first node only.here the address of the
last node is NULL.here structure is used to define a node.
addres of the next node can be stored in pointer variable.
for every node it allocates 8 bytes as it has integer(4) and the address(4)
vcruntime140.dll
'''
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
class SLinkedList:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval#1000
        while printval is not None:
            print(printval.dataval)#2000.dataval="tue"
            print(printval.nextval)
            printval = printval.nextval#2000.nextval="3000"
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list.headval.nextval = e2
#list.headval.nextval.nextval = e3
e2.nextval = e3
list.listprint()
