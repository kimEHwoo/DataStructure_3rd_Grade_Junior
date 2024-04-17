class Empty(Exception):
    pass

class LinkedQueue:

    class _Node:
        __slots__ = ['_element', '_next']

        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        return self._head._element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._element = newest
        self._tail = newest
        self._size += 1

    def dequeue(self, e):
        if self.is_empty():
            raise Empty('Queue is Empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer
    
    def __str__(self):
        arr = ''
        start = self._head
        for i in range(self._size):
            arr += str(start._element) + ', '
            start = start._next
        return '<' + arr + '<'
    
if __name__ == '__main__':
    Q = LinkedQueue()
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