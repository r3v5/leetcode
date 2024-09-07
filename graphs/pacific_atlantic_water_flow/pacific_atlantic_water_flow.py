from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        p_set = set()
        p_queue = deque()
        a_set = set()
        a_queue = deque()

        # process most up row for p ocean
        for j in range(n):
            p_set.add((0, j))
            p_queue.append([0, j])

        # process most left col for p ocean
        for i in range(1, m):
            p_set.add((i, 0))
            p_queue.append([i, 0])

        # process most right col for a ocean
        for i in range(m):
            a_set.add((i, n - 1))
            a_queue.append([i, n - 1])

        # process most bottom row for a ocean
        for j in range(n - 1):
            a_set.add((m - 1, j))
            a_queue.append([m - 1, j])

        def bfs(queue, visited) -> None:
            while queue:
                q_size = len(queue)

                for _ in range(q_size):
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

        bfs(p_queue, p_set)
        bfs(a_queue, a_set)

        return list(p_set.intersection(a_set))
