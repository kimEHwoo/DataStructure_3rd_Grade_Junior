# Matching Tags in a Markup Language (HTML Tags)

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

def is_matched_html(raw):
    '''return True if all HTML tags are properly match; False otherwise'''
    S = ArrayStack()
    j = raw.find('<')               # find => 첫 번째로 발견된 위치의 인덱스, not find => -1
    while j != -1:                  # find에서 < 찾은 경우
        k = raw.find('>', j+1)      # j+1부터 '>' 검색을 시작
        if k==-1:                   #
            print('Invalid Tag')
            return False
        tag = raw[j+1:k]            # j = <가 있는 index, k = >가 있는 index
        if not tag.startswith('/'): # HTML에서는 tag에 /로 시작하면 pop 역할을 함
            S.push(tag)
        else:                       # '/'가 있는 경우 'pop'
            if S.is_empty():
                print('Stack is empty. Nothing to match with')
                return False        # S(스택)에 여는 태그가 하나도 없다.
            if tag[1:] != S.pop():  # tag[1:]는 S에 들어가는 태그 하나(덩어리 하나)
                print('Tag Mismatch:', tag)
                return False
        j = raw.find('<', k+1)      # 다음 < 를 찾는다.
    return S.is_empty()
