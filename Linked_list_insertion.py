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
    #Insertion at the beginning          
    def AtBegining(self,newdata):
        NewNode = Node(newdata) #newnode=4000
        #Update the new nodes nextval to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode
    #Insertion at the end
    def AtEnd(self,newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval#last = 4000  if there is nextval so there is next node
        while(last.nextval):#1000,2000,3000 
            last = last.nextval#1000,2000,3000
        last.nextval=NewNode
    #Insertion in between
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)#6000
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode
    #Insertion at given position
    def 
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list.headval.nextval = e2
#list.headval.nextval.nextval = e3
e2.nextval = e3
list.AtBegining("Sun")
list.Inbetween(list.headval.nextval.nextval.nextval,"Thu")
list.AtEnd("Fri")
#list.insertAfter("Fri","Sat")
list.listprint()
