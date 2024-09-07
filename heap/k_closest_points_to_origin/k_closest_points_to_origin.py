import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        result = []

        for i in range(len(points)):

            # calculate distence based on formula: √(x1 - x2)^2 + (y1 - y2)^2
            distance = math.sqrt((points[i][0] - 0) ** 2 + (points[i][1] - 0) ** 2)

            # add distance and coordinates to heap array
            min_heap.append((distance, points[i][0], points[i][1]))

        # create heap with min_heap array
        heapq.heapify(min_heap)

        while k > 0:
            # get min distance from the top of the min heap
            min_distance = heapq.heappop(min_heap)
            coordinates = []

            x = min_distance[1]
            y = min_distance[2]

            coordinates.append(x)
            coordinates.append(y)

            result.append(coordinates)

            k -= 1

        return result


ex1 = [[1, 3], [-2, 2]]
k_ex1 = 1

ex2 = [[3, 3], [5, -1], [-2, 4]]
k_ex2 = 2

driver = Solution()
print(
    f"Example 1:\nInput: points = [[1, 3], [-2, 2]], k = 1\nOutput: {driver.kClosest(ex1, k_ex1)}\n"
)
print(
    f"Example 2:\nInput: points = [[3, 3], [5, -1],[-2, 4], k = 2\nOutput: {driver.kClosest(ex2, k_ex2)}\n"
)
