from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # value in matrix =  (i, j)
        # i = mid // num of cols
        # j = mid % num of cols

        rows = len(matrix)
        cols = len(matrix[0])
        total_nums = rows * cols
        l = 0
        r = total_nums - 1

        while l <= r:
            mid = (l + r) // 2

            # find val in matrix based on i and j
            i = mid // cols
            j = mid % cols

            if matrix[i][j] == target:
                return True

            if matrix[i][j] < target:
                l = mid + 1

            else:
                r -= 1

        return False

    # Time Complexity: O(log(m * n))
    # Space Complexity: O(1)
