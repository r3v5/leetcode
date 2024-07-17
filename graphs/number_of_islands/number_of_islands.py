from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0

        def dfs(i: int, j: int) -> None:
            # run dfs
            stack = [[i, j]]

            while stack:
                i, j = stack.pop()

                if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                    continue

                else:
                    # mark island as water to avoid revisiting
                    grid[i][j] = "0"
                    stack.append([i, j + 1])  # go right
                    stack.append([i, j - 1])  # go left
                    stack.append([i + 1, j])  # go down
                    stack.append([i - 1, j])  # go up

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)

        return islands

    # Time: O(m * n)
    # Space: O(m * n)


ex_1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

ex_2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

driver = Solution()

print(f"Example 1:\nInput: grid = {ex_1}\nOutput: {driver.numIslands(ex_1)}\n")
print(f"Example 2:\nInput: grid = {ex_2}\nOutput: {driver.numIslands(ex_2)}\n")
