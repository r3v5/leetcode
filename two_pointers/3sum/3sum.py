from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            # skip the cur element to avoid duplicates since it's the same value
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                if three_sum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # skip the cur element to avoid duplicates since it's the same value
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                elif three_sum < 0:
                    l += 1

                else:
                    r -= 1

        return result

    # Time Complexity: O(n^2)


ex_1 = [-1, 0, 1, 2, -1, -4]
ex_2 = [0, 1, 1]
ex_3 = [0, 0, 0]

driver = Solution()
print(f"Example 1:\nInput: nums = {ex_1}\nOutput: {driver.threeSum(ex_1)}\n")
print(f"Example 2:\nInput: nums = {ex_2}\nOutput: {driver.threeSum(ex_2)}\n")
print(f"Example 3:\nInput: nums = {ex_3}\nOutput: {driver.threeSum(ex_3)}\n")
