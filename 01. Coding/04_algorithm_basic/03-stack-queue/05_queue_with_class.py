class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if self.is_full(): # 가득 찼으면 더 못 넣음
            print('queue is full')
            return
        self.rear += 1
        self.items[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print('queue is empty')
            return
        self.front += 1


    def is_full(self):
        return self.rear == self.capacity-1

    def is_empty(self):
        return self.front == self.rear


    
# queue = Queue()

# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)

# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.items)
# print(queue.peek())

# queue.enqueue(4)
# queue.enqueue(5)

# print(queue.items)
# print(queue.is_full())
# queue.enqueue(11)