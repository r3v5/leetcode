class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}

        for i in range(len(s)):
            hashmap[s[i]] = 1 + hashmap.get(s[i], 0)

        for char, freq in hashmap.items():
            if freq == 1:
                return s.index(char)

        return -1

    # Time Complexity: O(n)
