import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Use Djikstra's algorithm

        # 1. build graph
        graph = defaultdict(list)  # source -> target, time

        for source, target, time in times:
            graph[source].append([target, time])

        # 2. create hashmap: node -> distance to reach it
        hashmap = {}

        # 3. init min heap: distance to node, node
        # since we start from given node, distance is 0
        min_heap = [[0, k]]

        # 4. Iterate through min heap
        while min_heap:
            distance, node = heapq.heappop(min_heap)

            if node in hashmap:
                continue

            hashmap[node] = distance

            # push neighbors to min heap
            for target, time in graph[node]:
                heapq.heappush(min_heap, [distance + time, target])

        if len(hashmap) == n:
            return max(hashmap.values())

        else:
            return -1

    # Time: O(V + E logV)
    # Space: O(V + E)
