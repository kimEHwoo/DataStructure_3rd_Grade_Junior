from collections import deque
class MaxQueue:
    def __init__(self):
        self.queue = deque()
        self.max_queue = deque()
    # queue는 queue를 담는 공간
    # max_queue는 queue 중에서 가장 큰 값

    def enqueue(self, value):
        self.queue.append(value)
        while self.max_queue and self.max_queue[-1]<value:
            # max_queue가 비어 있지 않다
            # & max_queue의 마지막 요소가 value 보다 작다
            # 즉 value가 가장 크다
            self.max_queue.pop()
        self.max_queue.append(value) # max_queue = value 최신화

    def dequeue(self):
        if not self.queue:
            return None
        value = self.queue.popleft()
        if value == self.max_queue[0]:
            self.max_queue.popleft()
        return value
    
    def max_value(self):
        if not self.max_queue:
            return None
        return self.max_queue[0]
    
    
max_queue = MaxQueue()
max_queue.enqueue(1)
max_queue.enqueue(3)
max_queue.enqueue(2)
print("Max value:", max_queue.max_value())
max_queue.dequeue()
print("Max value:", max_queue.max_value())
max_queue.dequeue()
print("Max value:", max_queue.max_value())        