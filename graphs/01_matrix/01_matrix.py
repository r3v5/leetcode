from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        queue = deque([])

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append([i, j])

                else:
                    mat[i][j] = float("inf")

        while queue:
            q_size = len(queue)
            for _ in range(q_size):
                i, j = queue.popleft()

                if j + 1 < n and mat[i][j + 1] > mat[i][j] + 1:
                    mat[i][j + 1] = mat[i][j] + 1
                    queue.append([i, j + 1])

                if j - 1 >= 0 and mat[i][j - 1] > mat[i][j] + 1:
                    mat[i][j - 1] = mat[i][j] + 1
                    queue.append([i, j - 1])

                if i + 1 < m and mat[i + 1][j] > mat[i][j] + 1:
                    mat[i + 1][j] = mat[i][j] + 1
                    queue.append([i + 1, j])

                if i - 1 >= 0 and mat[i - 1][j] > mat[i][j] + 1:
                    mat[i - 1][j] = mat[i][j] + 1
                    queue.append([i - 1, j])

        return mat


sol = Solution()


def test(mat: List[List[int]], exp: List[List[int]]) -> None:
    assert sol.updateMatrix(mat) == exp


test([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]])
test([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[0, 0, 0], [0, 1, 0], [1, 2, 1]])


"""
        0  1  2   
    0   [0, 0, 0]
    1   [0, 1, 0]
    2   [0, 0, 0]


BFS

base case: if nei.val > cur_cell.val + 1 then nei.val = cur_cell.val + 1

QUEUE
[1, 1] -> pop
[2, 2] -> pop
[2, 1] -> pop
[2, 0] -> pop
[1, 2] -> pop
[1, 0] -> pop
[0, 2] -> pop
[0, 1] -> pop
[0, 0] -> pop

Time: O(m * n)
Space: O(m * n)
"""
