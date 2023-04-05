'''
A train is identified by its name and list of compartments.The compartments are
identified by its name,total seating capacity and the number of passengers.
Implement the class Train as given in the class diagram.
Train
- train_name
- compartment_list
_init_(train_name,compartment_list)
+ get_train_name()
+ get_compartment_list()
+ count_compartments ()
+ check_vacancy()
Write a python program to implement the following:
count_compartments()- returns the total number of compartments in the train
check_vacancy()-returns the count of the compartments in which more than 50%
of the seats are vacant
Note : Compartment list is maintained as a linked list where data in each
node refers to a compartment.
'''



#Train Compartment

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class linkedList:
    def __init__(self):
        self.headval=None
    def listPrint(self):
        temp=self.headval
        while temp is not None:
            print(temp.data.comp_name,temp.data.t_seat,temp.data.n_pass)
            print()
            temp=temp.next

    def atHead(self,data):
        newnode=node(data)
        if(self.headval==None):
            self.headval=newnode
        else:
            newnode.next=self.headval
            self.headval=newnode
    def atEnd(self,data):
        newnode=Node(data)
        if(self.headval==None):
            self.headval=newnode
        else:
            temp=self.headval
            while(temp.next != None):
                temp=temp.next
            temp.next=newnode

    def length(self):
        cnt=0
        temp=self.headval
        while temp is not None:
            cnt+=1
            temp=temp.next
        print(cnt)
   
class Train:
    def __init__(self,tname,c_list):
        self.tname=tname
        self.c_list=c_list

    def get_train_name(self):
        return self.tname
    
    def get_compartment(self):
        self.c_list.listPrint()

    def count_compartment(self):
        self.c_list.length()
    
    def check_vacancy(self):
        temp=self.c_list.headval
        cnt=0
        while temp is not None:
            if(temp.data.t_seat-temp.data.n_pass >= temp.data.t_seat//2):
                cnt+=1
            temp=temp.next
        print(cnt)

class Compartment:
    def __init__(self,comp_name,n_pass,t_seat):
        self.comp_name=comp_name
        self.t_seat=t_seat
        self.n_pass=n_pass


list1=linkedList()
c1=Compartment("SL",250,400)
c2=Compartment("2AC",125,280)
c3=Compartment("3AC",120,300)
c4=Compartment("FC",160,300)
c5=Compartment("1AC",100,210)
list1.atEnd(c1)
list1.atEnd(c2)
list1.atEnd(c3)
list1.atEnd(c4)
list1.atEnd(c5)

t1=Train("Raja Rani",list1)
t1.count_compartment()
t1.check_vacancy()
t1.get_compartment()
print(t1.get_train_name())





