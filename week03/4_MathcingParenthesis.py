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


def is_matched(expr):

    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()

expr1 = '[(5+x)-(y+z)}'
print(is_matched(expr1))
expr2 = '[(5+x)-(y+z)]'
print(is_matched(expr2))