import heapq
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap = []
        result = []

        for i in range(len(arr)):
            diff = abs(x - arr[i])
            min_heap.append([diff, arr[i]])

        heapq.heapify(min_heap)

        while k > 0 and min_heap:
            diff, num = heapq.heappop(min_heap)
            result.append(num)
            k -= 1

        return self.quick_sort(result)

    # Time Complexity: O(nlogn + n)

    def quick_sort(self, arr: List[int]) -> List[int]:
        if len(arr) < 2:
            return arr

        else:
            pivot = arr[0]
            less = [num for num in arr[1:] if num <= pivot]
            greater = [num for num in arr[1:] if num > pivot]
            return self.quick_sort(less) + [pivot] + self.quick_sort(greater)
