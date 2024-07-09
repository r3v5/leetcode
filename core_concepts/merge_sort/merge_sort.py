from typing import List


class MergeSort:

    def merge(self, nums: List[int], l: int, mid: int, r: int) -> None:
        # calculate the lengths of tmp subarrays
        len_arr_1 = mid - l + 1
        len_arr_2 = r - mid

        # create tmp subarrays
        arr_1 = [0] * len_arr_1
        arr_2 = [0] * len_arr_2

        # populate the tmp subarrays by values from nums array
        for i in range(len_arr_1):
            arr_1[i] = nums[l + i]

        for j in range(len_arr_2):
            arr_2[j] = nums[mid + 1 + j]

        # merge two tmp subarrays
        i = 0
        j = 0
        k = l

        while i < len_arr_1 and j < len_arr_2:
            if arr_1[i] <= arr_2[j]:
                nums[k] = arr_1[i]
                i += 1

            else:
                nums[k] = arr_2[j]
                j += 1

            k += 1

        # check if some values left in one of tmp subarrays
        while i < len_arr_1:
            nums[k] = arr_1[i]
            i += 1
            k += 1

        while j < len_arr_2:
            nums[k] = arr_2[j]
            j += 1
            k += 1

        # Time complexity: O(n)

    def merge_sort(self, nums: List[int], l: int, r: int) -> None:
        if l < r:
            mid = (l + r) // 2

            self.merge_sort(nums, l, mid)
            self.merge_sort(nums, mid + 1, r)
            self.merge(nums, l, mid, r)

    # Overall Time Complexity: O(nlogn)


sorting = MergeSort()
arr = [12, 11, 13, 5, 6, 7]
print(arr)
sorting.merge_sort(arr, 0, 5)
print(arr)
