class CircularQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
            self.display()
        else:
            print("큐가 가득 찼습니다.")

    def dequeue(self):
        if not self.isEmpty():
            item = self.array[self.front + 1]
            self.array[self.front + 1] = None
            self.front = (self.front + 1) % self.capacity
            self.display()
            return item
        else:
            print("큐가 비어있습니다.")
            return None

    def display(self):
        print(f"Queue: {self.array}, Front: {self.front}, Rear: {self.rear}")


# 초기화
cq = CircularQueue()

# (1) enqueue(1)
cq.enqueue(1)

# (2) enqueue(2)
cq.enqueue(2)

# (3) enqueue(3)
cq.enqueue(3)

# (4) dequeue()
cq.dequeue()

# (5) enqueue(4)
cq.enqueue(4)




