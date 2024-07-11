from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        # (0) (1) (0) (3) (12)
        #  l   r
        # do swap and move left pointer if right pointer pointing to non zero integer
        # (1) (0) (0) (3) (12)
        #      l   r

        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                tmp = nums[r]
                nums[r] = nums[l]
                nums[l] = tmp
                l += 1

        return nums

    # Time Complexity: O(n)


ex_1 = [0, 1, 0, 3, 12]
ex_2 = [0]

driver = Solution()
print(f"Example 1:\nInput: nums = {ex_1}\nOutput: {driver.moveZeroes(ex_1)}\n")
print(f"Example 2:\nInput: nums = {ex_2}\nOutput: {driver.moveZeroes(ex_2)}\n")
