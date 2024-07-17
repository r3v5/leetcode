from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0

        def dfs(i: int, j: int) -> int:
            stack = [[i, j]]
            area = 0

            while stack:
                i, j = stack.pop()

                if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                    continue

                area += 1
                grid[i][j] = 0
                stack.append([i, j + 1])  # go right
                stack.append([i, j - 1])  # go left
                stack.append([i + 1, j])  # go down
                stack.append([i - 1, j])  # go up

            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area

    # Time: O(m * n)
    # Space: O(m * n)


ex_1 = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]
ex_2 = [[0, 0, 0, 0, 0, 0, 0, 0]]

driver = Solution()
print(f"Example 1:\nInput: grid = {ex_1}\nOutput: {driver.maxAreaOfIsland(ex_1)}\n")
print(f"Example 2:\nInput: grid = {ex_2}\nOutput: {driver.maxAreaOfIsland(ex_2)}\n")
