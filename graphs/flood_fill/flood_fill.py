from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        initial_color = image[sr][sc]

        def dfs(i: int, j: int) -> None:
            stack = [[i, j]]
            visited = set()

            while stack:
                i, j = stack.pop()

                if (
                    i < 0
                    or i >= m
                    or j < 0
                    or j >= n
                    or image[i][j] != initial_color
                    or (i, j) in visited
                ):
                    continue

                visited.add((i, j))
                image[i][j] = color
                stack.append([i, j + 1])  # go right
                stack.append([i, j - 1])  # go left
                stack.append([i + 1, j])  # go down
                stack.append([i - 1, j])  # go up

        dfs(sr, sc)

        return image

    # Time: O(m * n)
    # Space: O(m * n)


ex_1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
ex_1_sr = 1
ex_1_sc = 1
ex_1_color = 2

ex_2 = [[0, 0, 0], [0, 0, 0]]
ex_2_sr = 0
ex_2_sc = 0
ex_2_color = 0

driver = Solution()
print(
    f"Example 1:\nInput: image = {ex_1}, sr = {ex_1_sr}, sc = {ex_1_sc}, color = {ex_1_color}\nOutput: {driver.floodFill(ex_1, ex_1_sr, ex_1_sc, ex_1_color)}\n"
)
print(
    f"Example 2:\nInput: image = {ex_2}, sr = {ex_2_sr}, sc = {ex_2_sc}, color = {ex_2_color}\nOutput: {driver.floodFill(ex_2, ex_2_sr, ex_2_sc, ex_2_color)}\n"
)
