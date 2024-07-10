from typing import List

nums = [1, 8, 5, 2, 0]


def bubble_sort(nums: List[int]) -> List[int]:
    # go through the length of list - 1 since amount of pairs is length - 1
    for i in range(len(nums) - 1):

        # go through the pairs and don't check last sorted element or elements (i is indicating how much elements are already sorted)
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                tmp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = tmp

    return nums


# Time Complexity: O(n^2)

print(f"nums = {nums}\nSorted array: {bubble_sort(nums)}\n")
