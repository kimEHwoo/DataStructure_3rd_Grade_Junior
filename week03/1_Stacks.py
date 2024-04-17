# Stack
# Array-based Stack ADT
# The following Codes shows an implementation of stack using Python List
# We define a new exception type "Empty" more suitable in the context of Stack
# We define functions pop() and push() for adding and removing elements to and from the stack.

# define a new type of exception for stack ADT
class Empty(Exception):
    '''Error attempting to acces an element from an empty container.'''
    pass

class ArrayStack:
    '''LIFO stack implementation using a Python List as underlying storage'''
    def __init__(self): # constructor
        '''create an empty stack'''
        self._data = [] # nonpublic list instance

    def __len__(self):
        '''return the number of elements in a stack'''
        return len(self._data)
    
    def is_empty(self):
        '''Return True if the stack is empty'''
        return len(self._data) == 0
    
    def push(self, e):
        '''Add element e to the top of the stack'''
        self._data.append(e) # new item stored at end of a list

    def top(self):
        '''
        Return the element at the top of the stack
        Raise Empty Exception if the stack is empty
        '''
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._data[-1] # the last item in the list
    
    def pop(self):
        '''
        Remove and return the element from the top of the stack
        Raise Empty exception if the stack is empty
        '''
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._data.pop()
    
    def __str__(self):
        '''
        A string representation of the stack
        An arrow shows the top of the stack
        '''
        return ''.join(str(self._data)) + '>'
    

################
S = ArrayStack()
S.push(5)
S.push(3)
S.push(3)
print('Stack Length: ', len(S))
print('S: ', S)
print('Pop ', S.pop())
print('Is stack Empty? ', S.is_empty())
print('Pop ', S.pop())
print('Is stack Empty? ', S.is_empty())
print('S:', S)
S.push(7)
S.push(9)
print('Top Element in Stack: ', S.top())
S.push(4)
S.push(6)
print('S: ', S)