from collections import defaultdict, deque
from typing import List


class SolutionDFS:

    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        # base case
        if source == destination:
            return True

        # populate graph hashmap with nodes
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # dfs
        stack = [source]
        visited = set()
        visited.add(source)

        while stack:
            node = stack.pop()

            if node == destination:
                return True

            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)

        return False

    # Time: O(v + e)
    # Space: O(n)


class SolutionBFS:

    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        # base case
        if source == destination:
            return True

        # populate graph hashmap with nodes
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # bfs
        queue = deque([source])
        visited = set()
        visited.add(source)

        while queue:
            node = queue.popleft()

            if node == destination:
                return True

            else:
                # go through neighbours
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        queue.append(neighbour)
                        visited.add(neighbour)

        return False

    # Time: O(v + e)
    # Space: O(n)


ex_1 = [[0, 1], [1, 2], [2, 0]]
ex_1_source = 0
ex_1_destination = 2
ex_1_n = 3

ex_2 = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
ex_2_n = 6
ex_2_source = 0
ex_2_destination = 5

dfs = SolutionDFS()
bfs = SolutionBFS()
print(
    f"Example 1 using DFS:\nInput: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2\nOutput: {dfs.validPath(ex_1_n, ex_1, ex_1_source, ex_1_destination)}\n"
)
print(
    f"Example 1 using BFS:\nInput: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2\nOutput: {bfs.validPath(ex_1_n, ex_1, ex_1_source, ex_1_destination)}\n"
)
print(
    f"Example 2 using DFS:\nInput: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5\nOutput: {dfs.validPath(ex_2_n, ex_2, ex_2_source, ex_2_destination)}\n"
)
print(
    f"Example 2 using BFS:\nInput: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5\nOutput: {bfs.validPath(ex_2_n, ex_2, ex_2_source, ex_2_destination)}\n"
)
