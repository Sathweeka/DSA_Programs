'''
Write a python function which accepts two linked lists containing integer
data and an integer, n and merges the two linked lists, such that list2 is
merged with list1 after n number of nodes.
Assume that value of n will always be less than or equal to the number of
nodes in list1..
Sample      Input Expected Output,
list1         1->2->4->3->5
list2           9->8->11
n-2      1->2->9->8->11->4->3->5
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data,end=" ")
            printval = printval.next
    def insert(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
    def merge(self,n,list3):
        temp = self.head

        while temp is not None:
            if (n ==0):
                list3.listprint()
                n-=1
            else:
                print(temp.data,end =" ")
                temp = temp.next
                n -= 1

list1 = LinkedList()
list2 = LinkedList()
list(map(list1.insert,input().split()))
list(map(list2.insert,input().split()))
n = int(input())
list1.merge(n,list2)
