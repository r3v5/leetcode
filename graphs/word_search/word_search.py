from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 1. run dfs
        # 2. run through matrix

        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs(row: int, col: int, index: int) -> bool:
            # base case
            if index == len(word):
                return True

            # check if run out of matrix
            if (
                row < 0
                or col < 0
                or row >= rows
                or col >= cols
                or board[row][col] != word[index]
                or (row, col) in path
            ):
                return False

            # add cur char in path
            path.add((row, col))

            # move position to 4 sides
            result = (
                dfs(row + 1, col, index + 1)
                or dfs(row - 1, col, index + 1)
                or dfs(row, col + 1, index + 1)
                or dfs(row, col - 1, index + 1)
            )

            # remove char from path after backtracking
            path.remove((row, col))

            return result

        # run through matrix
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False
