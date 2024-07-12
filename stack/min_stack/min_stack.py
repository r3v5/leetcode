class MinStack:
    """
    stack = [-2, 0, -3]
    min_stack = [-2, -2, -3]
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def is_empty_min_stack(self) -> bool:
        if len(self.min_stack) == 0:
            return True

        else:
            return False

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.is_empty_min_stack():
            self.min_stack.append(val)

        else:
            if self.min_stack[-1] < val:
                self.min_stack.append(self.min_stack[-1])

            else:
                self.min_stack.append(val)

    def pop(self) -> None:
        if len(self.stack) > 0 and len(self.min_stack) > 0:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

    def __str__(self):
        return f"Stack: {list(self.stack)}\nMin Stack: {list(self.min_stack)}"

    # Time Complexity: O(1)


stacks = MinStack()
print(f"Initial stacks: {stacks}\n")

stacks.push(-2)
print(f"Stacks after push(-2): {stacks}\n")

stacks.push(0)
print(f"Stacks after push(0): {stacks}\n")

stacks.push(-3)
print(f"Stacks after push(-3): {stacks}\n")

min_val = stacks.getMin()
print(f"Min: {min_val}\n")

stacks.pop()
print(f"Stacks after pop(): {stacks}\n")

top_val = stacks.top()
print(f"Top of stack: {top_val}\n")

min_val = stacks.getMin()
print(f"Min: {min_val}\n")
