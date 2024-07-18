from collections import deque
from typing import Deque, List, Optional, Set


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # run bfs and find intersection of coordinates of two sets
        m = len(heights)
        n = len(heights[0])
        set_p = set()
        set_a = set()
        queue_p = deque([])
        queue_a = deque([])

        # up row in Pacific Ocean (water can flow from cell to ocean)
        for j in range(n):
            set_p.add((0, j))
            queue_p.append([0, j])

        # leftmost col in Pacific Ocean (water can flow from cell to ocean)
        # exclude (0, 0)
        for i in range(1, m):
            set_p.add((i, 0))
            queue_p.append([i, 0])

        # rightmost col in Atlantic Ocean (water can flow from cell to ocean)
        for i in range(m):
            set_a.add((i, n - 1))
            queue_a.append([i, n - 1])

        # bottom row in Atlantic Ocean (water can flow from cell to ocean)
        for j in range(n - 1):
            set_a.add((m - 1, j))
            queue_a.append([m - 1, j])

        # run bfs
        def bfs(queue: Optional[Deque], visited: Optional[Set]) -> None:
            while queue:
                i, j = queue.popleft()

                if (
                    j + 1 < n
                    and heights[i][j] <= heights[i][j + 1]
                    and (i, j + 1) not in visited
                ):
                    visited.add((i, j + 1))
                    queue.append([i, j + 1])

                if (
                    j - 1 >= 0
                    and heights[i][j] <= heights[i][j - 1]
                    and (i, j - 1) not in visited
                ):
                    visited.add((i, j - 1))
                    queue.append([i, j - 1])

                if (
                    i + 1 < m
                    and heights[i][j] <= heights[i + 1][j]
                    and (i + 1, j) not in visited
                ):
                    visited.add((i + 1, j))
                    queue.append([i + 1, j])

                if (
                    i - 1 >= 0
                    and heights[i][j] <= heights[i - 1][j]
                    and (i - 1, j) not in visited
                ):
                    visited.add((i - 1, j))
                    queue.append([i - 1, j])

        bfs(queue_p, set_p)
        bfs(queue_a, set_a)

        return list(set_p.intersection(set_a))

    # Time: O(m * n)
    # Space: O(m * n)
