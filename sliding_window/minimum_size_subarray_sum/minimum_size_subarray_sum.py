from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float("inf")
        l = 0
        window_sum = l

        for r in range(len(nums)):
            window_sum += nums[r]

            while window_sum >= target:
                result = min(result, r - l + 1)
                window_sum -= nums[l]
                l += 1

        if result == float("inf"):
            return 0

        else:
            return result

    # Time Complexity: O(n)


ex_1 = [2, 3, 1, 2, 4, 3]
ex_1_target = 7
ex_2 = [1, 4, 4]
ex_2_target = 4
ex_3 = [1, 1, 1, 1, 1, 1, 1, 1]
ex_3_target = 11

driver = Solution()
print(
    f"Example 1:\nInput: target = {ex_1_target}, nums = {ex_1}\nOutput: {driver.minSubArrayLen(ex_1, ex_1_target)}\n"
)
print(
    f"Example 2:\nInput: target = {ex_2_target}, nums = {ex_2}\nOutput: {driver.minSubArrayLen(ex_2, ex_2_target)}\n"
)
print(
    f"Example 3:\nInput: target = {ex_3_target}, nums = {ex_3}\nOutput: {driver.minSubArrayLen(ex_3, ex_3_target)}\n"
)
