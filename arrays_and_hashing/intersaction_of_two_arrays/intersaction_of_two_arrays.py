from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_1 = set(nums1)
        nums_2 = set(nums2)
        result = []

        for num in nums_1:
            if num in nums_2:
                result.append(num)

        return result


# Time Complexity: O(n)
