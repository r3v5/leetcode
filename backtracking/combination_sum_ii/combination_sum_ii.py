from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        stack = [[[], 0, 0]]  # combination, cur_sum, index
        candidates.sort()

        while stack:
            combination, cur_sum, index = stack.pop()

            if cur_sum == target:
                result.append(combination)

            if cur_sum > target:
                continue

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                new_combination = combination + [candidates[i]]
                new_cur_sum = cur_sum + candidates[i]
                stack.append([new_combination, new_cur_sum, i + 1])

        return result

    # Time: O(2 ** n)
    # Space: O(n)


ex_1 = [10, 1, 2, 7, 6, 1, 5]
ex_1_target = 8
ex_2 = [2, 5, 2, 1, 2]
ex_2_target = 5
driver = Solution()
print(
    f"Examle 1:\nInput: candidates = {ex_1}, target = {ex_1_target}\nOutput: {driver.combinationSum2(ex_1, ex_1_target)}\n"
)
print(
    f"Examle 2:\nInput: candidates = {ex_2}, target = {ex_2_target}\nOutput: {driver.combinationSum2(ex_2, ex_2_target)}\n"
)
