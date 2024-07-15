from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs(row: int, col: int, index: int) -> bool:
            # base case
            if index == len(word):
                return True

            # check if out of bound or mismatch in characters
            if (
                row < 0
                or col < 0
                or row >= rows
                or col >= cols
                or board[row][col] != word[index]
                or (row, col) in path
            ):
                return False

            path.add((row, col))

            result = (
                dfs(row + 1, col, index + 1)
                or dfs(row - 1, col, index + 1)
                or dfs(row, col + 1, index + 1)
                or dfs(row, col - 1, index + 1)
            )

            path.remove((row, col))

            return result

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False


ex_1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
ex_1_word = "ABCCED"
driver = Solution()
print(
    f"Example 1:\nInput: board = {ex_1}, word = {ex_1_word}\nOutput: {driver.exist(ex_1, ex_1_word)}\n"
)
