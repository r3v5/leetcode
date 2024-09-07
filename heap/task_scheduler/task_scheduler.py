import heapq
from collections import deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # hashmap for counting tasks
        hashmap = {}

        for i in range(len(tasks)):
            hashmap[tasks[i]] = 1 + hashmap.get(tasks[i], 0)

        # max heap for storing most frequent tasks
        max_heap = [-1 * task for task in hashmap.values()]
        heapq.heapify(max_heap)

        # queue for adding tasks for max heap to track the count left and idle time
        queue = deque([])

        # start with time = 0
        time = 0

        while max_heap or queue:

            time += 1

            # pop the task from max heap and add it to the queue
            if max_heap:
                count = 1 + heapq.heappop(max_heap)

                if count:
                    queue.append([count, time + n])

            # check if idle time of first task in queue is now
            if queue and time == queue[0][1]:
                heapq.heappush(max_heap, queue.popleft()[0])

        return time


ex1 = ["A", "A", "A", "B", "B", "B"]
n_ex1 = 2

ex2 = ["A", "C", "A", "B", "D", "B"]
n_ex2 = 1

ex3 = ["A", "A", "A", "B", "B", "B"]
n_ex3 = 3

driver = Solution()
print(
    f"Example 1:\nInput: {ex1}, n = {n_ex1}\nOutput: {driver.leastInterval(ex1, n_ex1)}\n"
)
print(
    f"Example 2:\nInput: {ex2}, n = {n_ex2}\nOutput: {driver.leastInterval(ex2, n_ex2)}\n"
)
print(
    f"Example 3:\nInput: {ex3}, n = {n_ex3}\nOutput: {driver.leastInterval(ex3, n_ex3)}\n"
)
