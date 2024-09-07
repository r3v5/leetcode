from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(i: int, j: int) -> None:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        i = 0
        l = 0
        r = len(nums) - 1

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1

            elif nums[i] == 2:
                swap(i, r)
                i -= 1
                r -= 1

            i += 1


"""
                 i
nums = [0, 0, 1, 1, 2, 2]
              l  r



while i < r

swap

if nums[i] = 0 then swap(l, i) and l+=1
if nums[i] == 2 then swap(i, r) and i -= 1 and r -= 1

Time: O(n)
Space: O(1)
"""
