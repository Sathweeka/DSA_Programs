'''
Given a stack of integers, write a python program that updates the input stack
such that all occurrences of the smallest values are at the bottom of the same.
for example:
input stack (top-bottom): 5 66 5 8 7
output: 66 8 7 5 5
'''
def sortStack ( stack ):
    tmpStack = createStack()
    while(isEmpty(stack) == False):
        tmp = top(stack)
        pop(stack)
        while(isEmpty(tmpStack) == False and
             int(top(tmpStack)) > int(tmp)):
            push(stack,top(tmpStack))
            pop(tmpStack)
        push(tmpStack,tmp)     
    return tmpStack
def createStack():
    stack = []
    return stack
def isEmpty( stack ):
    return len(stack) == 0
def push( stack, item ):
    stack.append( item )
def top( stack ):
    p = len(stack)
    return stack[p-1]
def pop( stack ):
    if(isEmpty( stack )):
        print("Stack Underflow ")
        exit(1)
    return stack.pop()
def prints(stack):
    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end = ' ')
    print()
stack = createStack()
push( stack, str(5) )
push( stack, str(66) )
push( stack, str(5) )
push( stack, str(8) )
push( stack, str(7) )
push( stack, str(68) )
print("Sorted numbers are: ")
sortedst = sortStack ( stack )
prints(sortedst)
