from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        stack = [[[], 0, 1]]  # combination, length, number

        while stack:
            combination, length, index = stack.pop()

            if length == k:
                result.append(combination)

            elif length > k:
                continue

            for i in range(index, n + 1):
                stack.append([combination + [i], length + 1, i + 1])

        return result

    # Time: O(n choose k)
    # Time: O(n)


ex_1_n = 4
ex_1_k = 2
ex_2_n = 1
ex_2_k = 1

driver = Solution()
print(
    f"Example 1:\nInput: n = {ex_1_n}, k = {ex_1_k}\nOutput: {driver.combine(ex_1_n, ex_1_k)}\n"
)
print(
    f"Example 2:\nInput: n = {ex_2_n}, k = {ex_2_k}\nOutput: {driver.combine(ex_2_n, ex_2_k)}\n"
)
