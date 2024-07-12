from math import ceil, floor
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] in "+-*/":

                # popping two last integers from stack and perform operation
                second_val = stack.pop()
                first_val = stack.pop()

                if tokens[i] == "+":
                    stack.append(first_val + second_val)

                if tokens[i] == "-":
                    stack.append(first_val - second_val)

                if tokens[i] == "*":
                    stack.append(first_val * second_val)

                if tokens[i] == "/":
                    division = first_val / second_val

                    if division < 0:
                        stack.append(ceil(division))

                    else:
                        stack.append(floor(division))

            else:
                stack.append(int(tokens[i]))

        return stack[-1]

    # Time Complexity: O(n)


driver = Solution()
ex_1 = ["2", "1", "+", "3", "*"]
ex_2 = ["4", "13", "5", "/", "+"]
ex_3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

print(f"Example 1:\nInput: tokens = {ex_1}\nOutput: {driver.evalRPN(ex_1)}\n")
print(f"Example 2:\nInput: tokens = {ex_2}\nOutput: {driver.evalRPN(ex_2)}\n")
print(f"Example 3:\nInput: tokens = {ex_3}\nOutput: {driver.evalRPN(ex_3)}\n")
