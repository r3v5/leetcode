from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        # run dfs to capture all bordered Os as T temporary values
        def dfs(i: int, j: int) -> None:
            stack = [[i, j]]

            while stack:
                i, j = stack.pop()

                if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != "O":
                    continue

                board[i][j] = "T"
                stack.append([i, j + 1])
                stack.append([i, j - 1])
                stack.append([i + 1, j])
                stack.append([i - 1, j])

        # run dfs to capture all bordered Os as T temporary values
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i in [0, m - 1] or j in [0, n - 1]):
                    dfs(i, j)

        # mark all non bordered Os as X
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"

        # Swap all temporary Ts back to bordered Os
        for i in range(m):
            for j in range(n):
                if board[i][j] == "T":
                    board[i][j] = "O"

    # Time: O(m * n)
    # Space: O(m * n)
