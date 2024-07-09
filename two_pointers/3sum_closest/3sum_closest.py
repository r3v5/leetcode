from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = float("inf")
        nums.sort()

        # since we will already check integers by left and right pointers
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                if three_sum == target:
                    return three_sum

                elif abs(target - three_sum) < abs(target - result):
                    result = three_sum

                elif three_sum < target:
                    l += 1

                else:
                    r -= 1

        return result

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
