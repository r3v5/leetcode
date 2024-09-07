from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 1. create stack
        # 2. run dfs and go through each num and calculate new sum and update combination
        result = []
        stack = [[[], 0, 0]]

        while stack:
            combination, cur_sum, cur_index = stack.pop()

            if cur_sum == target:
                result.append(combination)

            if cur_sum > target:
                continue

            for i in range(cur_index, len(candidates)):
                new_combination = combination + [candidates[i]]
                new_cur_sum = cur_sum + candidates[i]
                stack.append([new_combination, new_cur_sum, i])

        return result

    # Time: O(n ** t)
    # Space: O(n)


ex_1 = [2, 3, 6, 7]
ex_1_target = 7

ex_2 = [2, 3, 5]
ex_2_target = 8

ex_3 = [2]
ex_3_target = 1

driver = Solution()

print(
    f"Example 1:\nInput: candidates = [2,3,6,7], target = 7\nOutput: {driver.combinationSum(ex_1, ex_1_target)}\n"
)
print(
    f"Example 2:\nInput: candidates = [2,3,5], target = 8\nOutput: {driver.combinationSum(ex_2, ex_2_target)}\n"
)
print(
    f"Example 3:\nInput: candidates = [2], target = 1\nOutput: {driver.combinationSum(ex_3, ex_3_target)}\n"
)
