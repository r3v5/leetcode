from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # run dfs using stack
        result = []

        # stack = [subset, index]
        stack = [[[], 0]]

        while stack:
            cur_subset, index = stack.pop()
            result.append(cur_subset)

            # add new subsets to stack
            # increment i by 1 since we skip duplicates
            for i in range(index, len(nums)):
                stack.append([cur_subset + [nums[i]], i + 1])

        return result

    # Time: O(2 ** n)
    # Space: O(n)


ex_1 = [1, 2, 3]
driver = Solution()
print(f"Example 1:\nInput: nums = [1,2,3]\nOutput: {driver.subsets(ex_1)}\n")
