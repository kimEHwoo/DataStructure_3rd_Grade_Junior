class Empty(Exception):
    pass

class CircularQueue:
    class _Node:
        __slots__ = ['_element', '_next']
        
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element
    
    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element
    
    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next

    def __str__(self):
        arr = ''
        start = self._tail._next
        for i in range(self._size):
            arr += str(start._element) + ', '
            start = start._next
        return '<' + arr + '<'
    
if __name__ == '__main__':

    Q = CircularQueue()
    Q.enqueue(5)
    Q.enqueue(7)
    Q.enqueue(1)
    Q.enqueue(9)
    Q.enqueue(3)
    print('Queue Length: ', len(Q))
    print('Queue: ', Q)

    print('Removed: ', Q.dequeue())
    print('Removed: ', Q.dequeue())

    print('Queue Length: ', len(Q))
    print('Queue: ', Q)

    print('Rotate : '); Q.rotate();

    print('Queue Length: ', len(Q))
    print('Queue: ', Q)