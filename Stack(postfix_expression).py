#Postfix evaluation
class Evaluate:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
    def isEmpty(self):
        return True if self.top == -1 else False
    def peek(self):
        return self.array[-1]
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
    def push(self, op):
        self.top += 1#2
        self.array.append(op)#5 9
    def evaluatePostfix(self, exp):
        for i in exp: #"231*+9-"
            if i.isdigit():
                self.push(i)
            else:
                val1 = self.pop()#val1=1 9
                val2 = self.pop()#val2=3 5
                self.push(str(eval(val2 + i + val1)))
        return int(self.pop())
if __name__ == '__main__':
    exp = "231*+9-"
    obj = Evaluate(len(exp))
    print("postfix evaluation: %d" %(obj.evaluatePostfix(exp)))
                              
        
