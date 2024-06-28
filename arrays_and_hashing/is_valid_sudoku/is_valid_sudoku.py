from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]  # List of sets for columns
        cols = [set() for i in range(9)]  # List of sets for rows
        boxes = {}  # hashmap of sets for 3x3 sub-boxes

        for row in range(9):
            for col in range(9):

                if board[row][col] == ".":
                    continue

                else:

                    # Check for duplicates in the current row, column, and sub-box
                    if (
                        board[row][col] in rows[row]
                        or board[row][col] in cols[col]
                        or board[row][col] in boxes.get((row // 3, col // 3), set())
                    ):
                        return False

                    # Add the current number to the respective sets
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])

                    # Add to the sub-box set, create it if not exists
                    if (row // 3, col // 3) not in boxes:
                        boxes[(row // 3, col // 3)] = set()

                    boxes[(row // 3, col // 3)].add(board[row][col])

        return True


board1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

board2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

driver = Solution()

print(driver.isValidSudoku(board1))
print(driver.isValidSudoku(board2))
