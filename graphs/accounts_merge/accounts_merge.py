from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        email_to_name = {}
        result = []

        for account in accounts:
            name = account[0]

            for email in account[1:]:
                graph[email].add(account[1])
                graph[account[1]].add(email)
                email_to_name[email] = name

        visited = set()

        for email in graph:
            if email not in visited:
                stack = [email]
                visited.add(email)
                merged_list = []

                while stack:
                    node = stack.pop()
                    merged_list.append(node)

                    for nei in graph[node]:
                        if nei not in visited:
                            stack.append(nei)
                            visited.add(nei)

                result.append([email_to_name[email]] + sorted(merged_list))

        return result


"""
result = []
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]]

1. build graph
GRAPH
"johnsmith@mail.com": "johnsmith@mail.com"
"john_newyork@mail.com": "johnsmith@mail.com"
"johnsmith@mail.com": "john_newyork@mail.com"
"john00@mail.com": "johnsmith@mail.com"
"johnsmith@mail.com": "john00@mail.com"

email_to_name = {} => email -> name

2. dfs on graph

Time: O(n * m)
Space: O(n * m)
"""
