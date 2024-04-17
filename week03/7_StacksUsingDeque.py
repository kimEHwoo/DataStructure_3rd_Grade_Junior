from collections import deque

def create_stack():
    stack = deque()    #Creating empty deque
    return stack

# PUSH operation using append()
def push(stack, item):
    stack.append(item)


#POP operation
def pop(stack):
    if(stack):
        print('Element popped from stack:')
        print(stack.pop())
    else:
        print('Stack is empty')


#Displaying Stack
def show(stack):
    print('Stack elements are:')
    print(stack)

new_stack=create_stack()
push(new_stack,25)
push(new_stack,56)
push(new_stack,32)
show(new_stack)

pop(new_stack)
show(new_stack)