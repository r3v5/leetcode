from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []

        # build graph
        graph = defaultdict(list)

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        unvisited = 0
        visiting = 1
        visited = 2
        states = [unvisited] * numCourses

        def dfs(node: int) -> bool:
            if states[node] == visiting:
                return False

            elif states[node] == visited:
                return True

            states[node] = visiting

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            states[node] = visited
            result.append(node)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return result

    # Time: O(V + E)
    # Space: O(V + E)
