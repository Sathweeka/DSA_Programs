#Double- Linked list
'''
here DDl has prev and next with data at middle. 35,25,15,5
'''

class Node:
    def __init__(self, value):
        self.previous = None
        self.data = value
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def length(self):
        temp = self.head
        count = 0
        while temp is not None:
            temp = temp.next
            count += 1
        return count
    def printLinkedList(self):
        temp= self.head
        while temp is not None:
            print(temp.data,sep = ",")
            temp = temp.next
    def insertAtBeginning(self, value):#15
        new_node = Node(value)#2000
        if self.isEmpty():
            self.head = new_node#800.head=1000
        else:
            new_node.next = self.head#2000.next=1000
            self.head.previous = new_node#2000
            self.head = new_node
    def insertAtEnd(self, value):#15
        new_node = Node(value)#2000
        if self.isEmpty():
            self.insertAtBeginning(value)
        else:
            temp = self.head#1000
            while temp.next is not None:
                temp =temp.next
            temp.next = new_node
            new_node.previous = temp
    def insertAtPosition(self, value, position):
        temp = self.head#temp=1000
        count = 0
        while temp is not None:
            if count == position - 1:
                break
            count += 1
            temp = temp.next
        if position == 1:
            self.insertAtBeginning(value)
        elif temp is None:
            print("There are less than {}-1 elements in the linked list. Cannot insert at {} position.".format(position,position))
        elif temp.next is None:
            self.insertAtEnd(value)
        else:
            new_node = Node(value)
            new_node.next = temp.next
            new_node.previous = temp
            temp.next.previous = new_node
            temp.next = new_node
    def deleteFromBeginning(self):
        if self.isEmpty():
            print("Linked List is empty. Cannot delete elements.")
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.previous = None
    def deleteFromLast(self):
        if self.isEmpty():
            print("Linked List is empty. Cannot delete elements.")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next is not None:#3000 4000
                temp = temp.next#4000
            temp.previous.next = None#3000.next=None
            temp.previous = None
    def deleteFromPosition(self, position):
        if self.isEmpty():
            print("Linked List is empty.cannot delete elements.")
        elif position == 1:
            self.deleteFromBeginning()
        else:
            temp = self.head#1000
            count = 1
            while temp is not None:
                if count == position:
                    break
                temp = temp.next
                count = count+1
            if temp is None:
                print("There are less than {} elementsin linked list. Cannot delete element.".format(position))
                return
            elif temp.next is None:
                self.deleteFromLast()
                return
            temp.previous.next = temp.next#1000.next=3000
            temp.next.previous = temp.previous#3000.previous=1000
            temp.nxt = None
   
x = DoublyLinkedList()
print(x.isEmpty())
x.insertAtBeginning(5)
x.printLinkedList()
print(x.isEmpty())
x.insertAtBeginning(15)
x.insertAtBeginning(25)
x.insertAtBeginning(35)
x.insertAtEnd(45)
x.printLinkedList()
print("no of nodes",x.length())
print("Insert at position 2 and 8")
x.insertAtPosition(8, 2)
#x.printLinkedList()
print("delete from the beginning")
x.deleteFromBeginning()
x.printLinkedList()
print("delete at the last")
x.deleteFromLast()
x.printLinkedList()
print("delete data at 2nd position")
x.deleteFromPosition(2)
x.printLinkedList()

