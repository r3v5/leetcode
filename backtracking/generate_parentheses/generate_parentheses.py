from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        # dfs for backtracking
        # stack: cur sequence, open brackets, close brackets
        # to add close brackets, we require close < open
        stack = [["", 0, 0]]
        while stack:
            cur_seq, open_brackets, close_brackets = stack.pop()

            if open_brackets == close_brackets == n:
                result.append(cur_seq)

            if close_brackets < open_brackets:
                stack.append([cur_seq + ")", open_brackets, close_brackets + 1])

            if open_brackets < n:
                stack.append([cur_seq + "(", open_brackets + 1, close_brackets])

        return result

    # Time Complexity: O(2n/n)


ex_1 = 3
ex_2 = 1

driver = Solution()
print(f"Example 1:\nInput: n = {ex_1}\nOutput: {driver.generateParenthesis(ex_1)}\n")
print(f"Example 2:\nInput: n = {ex_2}\nOutput: {driver.generateParenthesis(ex_2)}\n")
