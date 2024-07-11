from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l <= r:
            cur_sum = numbers[l] + numbers[r]

            if cur_sum == target:
                return [l + 1, r + 1]

            elif cur_sum < target:
                l += 1

            else:
                r -= 1

    # Time Complexity: O(n)


ex_1 = [2, 7, 11, 15]
ex_1_target = 9
ex_2 = [2, 3, 4]
ex_2_target = 6
ex_3 = [-1, 0]
ex_3_target = -1

driver = Solution()
print(
    f"Example 1:\nInput: numbers = {ex_1}, target = {ex_1_target}\nOutput: {driver.twoSum(ex_1, ex_1_target)}\n"
)
print(
    f"Example 2:\nInput: numbers = {ex_2}, target = {ex_2_target}\nOutput: {driver.twoSum(ex_2, ex_2_target)}\n"
)
print(
    f"Example 3:\nInput: numbers = {ex_3}, target = {ex_3_target}\nOutput: {driver.twoSum(ex_3, ex_3_target)}\n"
)
