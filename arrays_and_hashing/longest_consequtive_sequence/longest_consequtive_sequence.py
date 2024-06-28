from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use set for storing numbers

        longest = 0
        sequence = set(nums)

        for i in range(len(nums)):

            if (nums[i] - 1) not in sequence:
                length = 0

                while nums[i] + length in sequence:
                    length += 1

                longest = max(longest, length)

        return longest


nums1 = [100, 4, 200, 1, 3, 2]
nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
driver = Solution()
print(driver.longestConsecutive(nums1))
print(driver.longestConsecutive(nums2))
