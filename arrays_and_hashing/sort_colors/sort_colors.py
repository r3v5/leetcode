from typing import List


class SolutionBubbleSort:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.bubble_sort(nums)

    def bubble_sort(self, nums: List[int]) -> None:
        # go through the length of list - 1 since amount of pairs is length - 1
        for i in range(len(nums) - 1):

            # go through the pairs and don't check last sorted element or elements (i is indicating how much elements are already sorted)
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    tmp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = tmp

    # Time Complexity: O(n^2)


class SolutionQuickSort:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums = self.quick_sort(nums)

        # modifies the list in place
        nums[:] = sorted_nums

    def quick_sort(self, nums: List[int]) -> List[int]:
        # base case if array is already sorted
        if len(nums) < 2:
            return nums

        else:
            pivot = nums[0]
            less = [num for num in nums[1:] if num <= pivot]
            greater = [num for num in nums[1:] if num > pivot]

            return self.quick_sort(less) + [pivot] + self.quick_sort(greater)

    # Avearge Time Complexity: O(nlogn)
    # Worst Case: O(n^2)


ex_1 = [2, 0, 2, 1, 1, 0]
ex_2 = [2, 0, 1]
ex_3 = [1, 8, 5, 2, 0]

bubble_sort_solution = SolutionBubbleSort()
quick_sort_solution = SolutionQuickSort()
print("Bubble Sort Solution:\n")
print(
    f"Example 1:\nInput: {ex_1}\nOutput: {bubble_sort_solution.sortColors(ex_1)} and {ex_1}\n"
)
print(
    f"Example 2:\nInput: {ex_2}\nOutput: {bubble_sort_solution.sortColors(ex_2)} and {ex_2}\n"
)
print(
    f"Example 3:\nInput: {ex_3}\nOutput: {bubble_sort_solution.sortColors(ex_3)} and {ex_3}\n"
)

ex_1 = [2, 0, 2, 1, 1, 0]
ex_2 = [2, 0, 1]
ex_3 = [1, 8, 5, 2, 0]
print("Quick Sort Solution:\n")
print(
    f"Example 1:\nInput: {ex_1}\nOutput: {quick_sort_solution.sortColors(ex_1)} and {ex_1}\n"
)
print(
    f"Example 1:\nInput: {ex_2}\nOutput: {quick_sort_solution.sortColors(ex_2)} and {ex_2}\n"
)
print(
    f"Example 1:\nInput: {ex_3}\nOutput: {quick_sort_solution.sortColors(ex_3)} and {ex_3}\n"
)
