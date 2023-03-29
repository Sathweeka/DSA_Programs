"""
Given two queues,one integer queue and other character queue, write a python
to merge them to form a single queue. Follow the below rules for merging:
Merge elements at the same position starting with the integer queue.
If one of the queues has more elements than the other, add all the additional
elements at the end of the output queue.
Note: max_size of the merged queue should be the sum of the size of both
the queues.
for example,
Input--queue1: 3,6,8    queue2: b,y,u,t,r,o
Output-- 3,b,6,y,8,u,t,r,o
"""

class queue:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.queue=[None]*self.maxsize
        self.rear=-1
        self.front=0

    def is_full(self):
        if self.rear==self.maxsize-1:
            print(' the queue is full')
        return False
    def is_empty(self):
        if self.front>self.rear:
            return True
        return False
    def enqueue(self,data):
        if self.is_full():
            print(' queue is full')
        else:
            self.rear+=1
            self.queue[self.rear]=data

    def dequeue(self):
        if self.is_empty():
            print('queue is empty')
        else:
            data=self.queue[self.front]
            self.front+=1
            return data
    def display(self):
        for ind in range(self.front,self.rear+1):
            
        
                print(self.queue[ind])        
    def max_size(self):
        return self.maxsize

q=queue(3)
q.enqueue(3)
q.enqueue(6)
q.enqueue(8)
p=queue(6)
p.enqueue('b')
p.enqueue('y')
p.enqueue('u')
p.enqueue('t')
p.enqueue('r')
p.enqueue('o')
q3=queue(q.max_size()+p.max_size())
q3.display()

while q.rear>=q.front and p.rear>=p.front:
    q3.enqueue(q.queue[q.front])
    q3.enqueue(p.queue[p.front])
    q.front+=1
    p.front+=1
while(q.front<=q.rear):
    q3.enqueue(p.queue[p.front])
    q.front+=1
while(p.front<p.rear):
    q3.enqueue(p.queue[p.front])
    p.front+=1

q3.display()
    

