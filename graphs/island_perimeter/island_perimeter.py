from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        def dfs(i: int, j: int) -> int:
            stack = [[i, j]]
            visited = set()
            perimeter = 0

            while stack:
                i, j = stack.pop()

                if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == 0:
                    perimeter += 1
                    continue

                if (i, j) in visited:
                    continue

                else:
                    visited.add((i, j))
                    stack.append([i, j + 1])
                    stack.append([i, j - 1])
                    stack.append([i + 1, j])
                    stack.append([i - 1, j])

            return perimeter

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return dfs(i, j)

    # Time: O(m * n)
    # Space: O(m * n)


ex_1 = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
ex_2 = [[1]]
ex_3 = [[1, 0]]

driver = Solution()
print(f"Example 1:\nInput: grid = {ex_1}\nOutput: {driver.islandPerimeter(ex_1)}\n")
print(f"Example 2:\nInput: grid = {ex_2}\nOutput: {driver.islandPerimeter(ex_2)}\n")
print(f"Example 3:\nInput: grid = {ex_3}\nOutput: {driver.islandPerimeter(ex_3)}\n")
