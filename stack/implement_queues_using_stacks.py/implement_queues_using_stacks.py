class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop(0)

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True

        else:
            return False

    def __str__(self):
        return f"{list(self.queue)}"

    # Time Complexity: O(1)


queue = MyQueue()
print(f"Initial queue: {queue}\n")

queue.push(1)
print(f"Queue after push(1): {queue}\n")

queue.push(2)
print(f"Queue after push(2): {queue}\n")

param_3 = queue.peek()
print(f"Top of the queue: {param_3}\n")

queue.pop()
print(f"Queue after pop(): {queue}\n")

param_4 = queue.empty()
print(f"Is queue empty: {param_4}\n")
