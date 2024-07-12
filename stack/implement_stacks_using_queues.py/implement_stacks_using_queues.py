from collections import deque


class MyStack:

    def __init__(self):
        self.stack = deque([])

    # O(1)
    def push(self, x: int) -> None:
        self.stack.append(x)

    # O(1)
    def pop(self) -> int:
        return self.stack.pop()

    # O(1)
    def top(self) -> int:
        if not self.empty():
            return self.stack[-1]

    # O(1)
    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True

        else:
            return False

    def __str__(self):
        return f"{list(self.stack)}"


stack = MyStack()
print(f"Initial stack: {stack}\n")

stack.push(1)
print(f"Stack after push(1): {stack}\n")

stack.push(2)
print(f"Stack after push(2): {stack}\n")

param_3 = stack.top()
print(f"Top of the stack: {param_3}\n")

stack.pop()
print(f"Stack after pop(): {stack}\n")

param_4 = stack.empty()
print(f"Is stack empty: {param_4}\n")
