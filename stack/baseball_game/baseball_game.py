from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in range(len(operations)):
            if operations[i] in "+DC":

                if len(stack) != 0:

                    if operations[i] == "C":
                        stack.pop()

                    if operations[i] == "D":
                        stack.append(stack[-1] * 2)

                    if operations[i] == "+":
                        stack.append(stack[-2] + stack[-1])
            else:
                stack.append(int(operations[i]))

        return sum(stack)

    # Time Complexity: O(n)
    # Space Complexity: O(n)


ex_1 = ["5", "2", "C", "D", "+"]
ex_2 = ["5", "-2", "4", "C", "D", "9", "+", "+"]
ex_3 = ["1", "C"]

driver = Solution()
print(f"Example 1:\nInput ops = {ex_1}\nOutput: {driver.calPoints(ex_1)}\n")
print(f"Example 2:\nInput ops = {ex_2}\nOutput: {driver.calPoints(ex_2)}\n")
print(f"Example 3:\nInput ops = {ex_3}\nOutput: {driver.calPoints(ex_3)}\n")
