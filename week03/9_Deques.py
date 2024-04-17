class Empty(Exception):
    """Queue is empty."""
    pass


class ArrayDeque:
    '''
    FIFO Queue implementation using a Python List as underlying storage
    '''
    DEFAULT_CAPACITY = 5
    def __init__(self):
        '''Create an empty deque'''
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        self._rear = 0

    def __len__(self):
        return self._size
    
    def first(self):
        if self.is_empty():
            raise Empty('Deque is Empty')
        return self._data[self._front]
    
    def last(self):
        if self.is_empty():
            raise Empty('Deque is Empty')
        return self._data[self._rear]
    
    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        self._front = (self._front-1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def add_last(self, e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        self._rear = (self.front+1) % len(self._data)
        self._data[self._rear] = e
        self._size += 1

    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        return answer
    
    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        answer = self._data[self._rear]
        self._data[self._rear] = None
        self._rear = (self._rear - 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        return answer
    
    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk) % len(old)
        self._front = 0
        self._rear = self._size -1

    def __str__(self):
        return '<' + ''.join(str(self._data)) + '<'
    


import collections

d = collections.deque('abcdefg')
print('Deque:', d)
print('Length:', len(d))
print('Left end:', d[0])
print('Right end:', d[-1])

d.remove('c')
print('remove(c):', d)

D = collections.deque()
D.appendleft(5)
D.appendleft(6)
D.append(10)
D.append(2)
D.appendleft(3)
D.appendleft(7)
print('Deque D: ', D)
print('Length: ', len(D))
D.rotate(5) #circularly shift rightward k steps
print('Deque D: ', D)
D.popleft()
D.pop()
print('Deque D: ', D)
print('Length: ', len(D))

D = collections.deque()
D.appendleft(7)
D.appendleft(3)
D.append(6)
D.append(8)
D.appendleft(5)
D.appendleft(4)
print('Deque D: ', D)
print('Length: ', len(D))
D.rotate(5) #circularly shift rightward k steps
print('Deque D: ', D)
D.popleft()
print('Deque D: ', D)
print('Length: ', len(D))