class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):#1000 2000
            next = current.next#2000 3000
            current.next = prev#None 1000
            prev = current#1000 2000
            current = next#2000 3000
        self.head = prev
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
list = LinkedList()
list.push(20)
list.push(4)
list.push(15)
list.push(85)
print ("Given linked list")
list.printList()
list.reverse()
print("\nReversed linked list")
list.printList()
