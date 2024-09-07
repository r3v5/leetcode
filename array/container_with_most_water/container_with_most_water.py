from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = float("-inf")
        l = 0
        r = len(height) - 1

        while l < r:
            cur_width = r - l
            cur_height = min(height[l], height[r])
            max_area = max(max_area, cur_width * cur_height)

            if height[l] < height[r]:
                l += 1

            else:
                r -= 1

        return max_area

    # Time Complexity: O(n)


ex_1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
ex_2 = [1, 1]
driver = Solution()
print(f"Example 1:\nInput: height = {ex_1}\nOutput: {driver.maxArea(ex_1)}\n")
print(f"Example 2:\nInput: height = {ex_2}\nOutput: {driver.maxArea(ex_2)}\n")
