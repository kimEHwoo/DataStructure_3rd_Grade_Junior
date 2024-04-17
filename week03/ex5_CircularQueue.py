class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def enqueue(self, item):
        if self.is_full():
            return False
        self.queue[self.rear] = item
        self.rear = (self.rear+1)%self.capacity
        self.size+=1
        return True
    
    def dequeue(self):
        if self.is_empty():
            return False
        item = self.queue[self.front]
        self.front = (self.front+1)%self.capacity
        self.size -= 1
        return item
    
    
cq = CircularQueue(5)
print(cq.is_empty())
print(cq.is_full())
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
print(cq.dequeue())
cq.enqueue(4)
cq.enqueue(5)
print(cq.is_full())
print(cq.enqueue(6))
print(cq.dequeue())