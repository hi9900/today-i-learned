class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("Queue is empty")

    def size(self):
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Queue is empty")
    
    def __repr__(self) -> str:
        return repr(self.items)

if __name__ == "__main__":
    queue = Queue()
    print(f"큐가 비었나요? {queue.isEmpty()}")
    print("큐에 숫자 0 ~ 9 추가")
    for i in range(10):
        queue.enqueue(i)
    print(f"큐 크기: {queue.size()}")
    print(f"peek: {queue.peek()}")
    print(f"dequeue: {queue.dequeue()}")
    print(f"peek: {queue.peek()}")
    print(queue)
