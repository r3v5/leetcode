import heapq


class MedianFinder:

    def __init__(self):
        self.small = []  # max heap
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)

        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.large) - len(self.small) > 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

        elif len(self.small) - len(self.large) > 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]

        elif len(self.small) > len(self.large):
            return -1 * self.small[0]

        return (-1 * self.small[0] + self.large[0]) / 2

    # Time Complexity: O(log(n))


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())
medianFinder.addNum(3)
print(medianFinder.findMedian())
