from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 3):

            # skip dupliactes checks
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 2):

                # skip dupliactes checks as well
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l = j + 1
                r = len(nums) - 1

                while l < r:

                    cur_sum = nums[i] + nums[j] + nums[l] + nums[r]

                    if cur_sum == target:
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                    elif cur_sum < target:
                        l += 1

                    else:
                        r -= 1

        return result

    # Time Complexity: O(n^3)


ex_1 = [1, 0, -1, 0, -2, 2]
ex_1_target = 0
ex_2 = [2, 2, 2, 2, 2]
ex_2_target = 8

driver = Solution()
print(
    f"Example 1:\nInput: nums = [1,0,-1,0,-2,2], target = 0\nOutput: {driver.fourSum(ex_1, ex_1_target)}\n"
)
print(
    f"Example 2:\nInput: nums = [2,2,2,2,2], target = 8\nOutput: {driver.fourSum(ex_2, ex_2_target)}\n"
)
