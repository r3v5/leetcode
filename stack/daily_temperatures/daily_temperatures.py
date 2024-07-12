from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [73,74,75,71,69,72,76,73]
        # if 74 > top of stack, 73, pop it and calculate the diff between positions
        # stack = [73]

        result = [0] * len(temperatures)

        # [temperature, index]
        stack = []

        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                index = stack.pop()[1]
                result[index] = i - index

            stack.append([val, i])

        return result

    # Time Complexity: O(n)


ex_1 = [73, 74, 75, 71, 69, 72, 76, 73]
ex_2 = [30, 40, 50, 60]
ex_3 = [30, 60, 90]

driver = Solution()
print(
    f"Example 1:\nInput: temperatures = {ex_1}\nOutput: {driver.dailyTemperatures(ex_1)}\n"
)
print(
    f"Example 2:\nInput: temperatures = {ex_2}\nOutput: {driver.dailyTemperatures(ex_2)}\n"
)
print(
    f"Example 3:\nInput: temperatures = {ex_3}\nOutput: {driver.dailyTemperatures(ex_3)}\n"
)
