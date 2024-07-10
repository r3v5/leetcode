from typing import List

nums = [2, 0, 2, 1, 1, 0]


def quick_sort(nums: List[int]) -> List[int]:
    # base case
    if len(nums) < 2:
        return nums

    else:
        pivot = nums[0]
        less = [num for num in nums[1:] if num <= pivot]
        greater = [num for num in nums[1:] if num > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


# Avearge Time Complexity: O(nlogn)
# Worst Case: O(n^2)

print(quick_sort(nums))
