from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        result = []
        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3
        RIGHT_WALL = n
        BOTTOM_WALL = m
        LEFT_WALL = -1
        UP_WALL = 0
        direction = RIGHT
        i = 0
        j = 0

        while len(result) != m * n:
            if direction == RIGHT:
                while j < RIGHT_WALL:
                    result.append(matrix[i][j])
                    j += 1

                j -= 1
                i += 1
                RIGHT_WALL -= 1
                direction = DOWN

            elif direction == DOWN:
                while i < BOTTOM_WALL:
                    result.append(matrix[i][j])
                    i += 1

                i -= 1
                j -= 1
                BOTTOM_WALL -= 1
                direction = LEFT

            elif direction == LEFT:
                while j > LEFT_WALL:
                    result.append(matrix[i][j])
                    j -= 1

                j += 1
                i -= 1
                LEFT_WALL += 1
                direction = UP

            else:

                while i > UP_WALL:
                    result.append(matrix[i][j])
                    i -= 1

                i += 1
                j += 1
                UP_WALL += 1
                direction = RIGHT

        return result


"""               0  1  2
               0 [1, 2, 3] 
               1 [4, 5, 6]
               2 [7, 8, 9]
                    

result = []

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
direction = RIGHT

RIGHT_WALL = n
BOTTOM_WALL = m
LEFT_WALL = -1
UP_WALL = 0

Time: O(m * n)
Space: O(m * n)

"""
