from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mins = -1
        queue = deque([])
        fresh_count = 0

        for i in range(m):
            for j in range(n):

                # find the first rotten orange
                if grid[i][j] == 2:
                    queue.append([i, j])

                elif grid[i][j] == 1:
                    fresh_count += 1

        # Since there are already no fresh oranges at minute 0, the answer is just 0.
        if fresh_count == 0:
            return 0

        # run bfs
        while queue:

            q_size = len(queue)

            for _ in range(q_size):

                i, j = queue.popleft()

                if j + 1 < n and grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    fresh_count -= 1
                    queue.append([i, j + 1])

                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    fresh_count -= 1
                    queue.append([i, j - 1])

                if i + 1 < m and grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2
                    fresh_count -= 1
                    queue.append([i + 1, j])

                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    grid[i - 1][j] = 2
                    fresh_count -= 1
                    queue.append([i - 1, j])

            mins += 1

        if fresh_count == 0:
            return mins

        return -1
