from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        len_nums1 = m
        len_nums2 = n
        result_size = len_nums1 + len_nums2
        result = [0] * result_size

        i = 0
        j = 0
        k = 0

        while i < len_nums1 and j < len_nums2:
            if nums1[i] <= nums2[j]:
                result[k] = nums1[i]
                i += 1

            else:
                result[k] = nums2[j]
                j += 1

            k += 1

        while i < len_nums1:
            result[k] = nums1[i]
            i += 1
            k += 1

        while j < len_nums2:
            result[k] = nums2[j]
            j += 1
            k += 1

        nums1[:] = result

        return nums1
        # Time Complexity: O(n)


ex_1_nums1 = [1, 2, 3, 0, 0, 0]
ex_1_nums2 = [2, 5, 6]
ex_1_m = 3
ex_1_n = 3

ex_2_nums1 = [1]
ex_2_nums2 = []
ex_2_n = 0

driver = Solution()
print(
    f"Example 1:\nInput: nums1 = {ex_1_nums1}, m = {ex_1_m}, nums2 = {ex_1_nums2}, n = {ex_1_n}\nOutput: {driver.merge(ex_1_nums1, ex_1_m, ex_1_nums2, ex_1_n)}\n"
)
