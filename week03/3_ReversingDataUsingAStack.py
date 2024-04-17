class Empty(Exception):
  ''' Error attempting to access an element from an empty container.'''
  pass

class ArrayStack:
  ''' LIFO stack implementation using a Python List as underlying storage'''

  def __init__(self):# constructor
    ''' create an empty stack'''
    self._data = []    # nonpublic list instance

  def __len__(self):
    ''' return the number of elements in a stack'''
    return len(self._data)

  def is_empty(self):
    ''' Return True if the stack is empty'''
    return len(self._data) == 0

  def push(self, e):
    ''' Add element e to the top of the stack'''
    self._data.append(e)  # new item stored at end of a list

  def top(self):
    '''
    Return the element at the top of the stack
    Raise Empty Exception if the stack is empty
    '''
    if self.is_empty():
      raise Empty('Stack is Empty')
    return self._data[-1]           # the last item in the list

  def pop(self):
    '''
    Remove and return the element from the top of the stack
    Raise Empty excepion if the stack is empty
    '''
    if self.is_empty():
      raise Empty('Stack is Empty')
    return self._data.pop()

  def __str__(self):
    '''
    A string representation of the stack
    An arrow shows the top of the stack
    '''
    return ''.join(str(self._data)) +'>'

# reversing Data Using A Stack
def reverse_file(filename):
  
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n)'))
    original.close()

    output = open(filename, 'w') # 파일을 쓰기 모드로 연다.
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()