from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque([])
        fresh = 0
        time = -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j])

                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        while queue:
            len_q = len(queue)

            for _ in range(len_q):

                i, j = queue.popleft()

                if j + 1 < n and grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    fresh -= 1
                    queue.append([i, j + 1])

                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    fresh -= 1
                    queue.append([i, j - 1])

                if i + 1 < m and grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2
                    fresh -= 1
                    queue.append([i + 1, j])

                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    grid[i - 1][j] = 2
                    fresh -= 1
                    queue.append([i - 1, j])

            time += 1

        if fresh == 0:
            return time

        else:
            return -1


"""       0 1 2
       0 [2,2,2]
       1 [2,2,0]
       2 [0,2,2]

fresh = 0
time = 4

QUEUE
0, 0 -> pop
0, 1 -> pop
1, 0 -> pop
1, 1 -> pop


Time: O(m * n)
Space: O(m * n)

"""
