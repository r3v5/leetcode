from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)  # node -> neighbors

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        unvisited = 0
        states = [unvisited] * numCourses
        visiting = 1
        visited = 2

        def dfs(node: int) -> bool:
            # has no neighbors
            if states[node] == visited:
                return True

            # there is a cycle
            if states[node] == visiting:
                return False

            states[node] = visiting

            # process neighbours
            for nei in graph[node]:
                if not dfs(nei):
                    return False

            # it means we can pass the course
            states[node] = visited
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

    # Time: O(V + E)
    # Space: O(V + E)
