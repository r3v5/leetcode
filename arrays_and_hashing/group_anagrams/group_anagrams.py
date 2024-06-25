from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # our task is to find the same pattern for different strings
        # the same amount of letters
        # we need to use hashmap for pattern and words

        hashmap = {}

        for word in strs:
            counter = [0] * 26

            for char in word:
                counter[ord(char) - ord("a")] += 1

            key = tuple(counter)

            if key not in hashmap:
                hashmap[key] = []

            hashmap[key].append(word)

        return hashmap.values()


driver = Solution()
print(list(driver.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])))
print(list(driver.groupAnagrams([""])))
print(list(driver.groupAnagrams(["a"])))
