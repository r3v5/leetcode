from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float("-inf")

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]

                if cur_sum == target:
                    return cur_sum

                elif abs(target - cur_sum) < abs(target - closest_sum):
                    closest_sum = cur_sum

                elif cur_sum < target:
                    l += 1

                elif cur_sum > target:
                    r -= 1

        return closest_sum

        # Time Complexity: O(n^2)


ex_1 = [-1, 2, 1, -4]
target_ex_1 = 1

ex_2 = [0, 0, 0]
target_ex_2 = 1

driver = Solution()
print(
    f"Example 1:\nInput: nums = {ex_1}, target = {target_ex_1}\nOutput: {driver.threeSumClosest(ex_1, target_ex_1)}\n"
)
print(
    f"Example 2:\nInput: nums = {ex_2}, target = {target_ex_2}\nOutput: {driver.threeSumClosest(ex_2, target_ex_2)}\n"
)
