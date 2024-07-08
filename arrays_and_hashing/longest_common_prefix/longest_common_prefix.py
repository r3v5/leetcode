from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float("inf")

        # find min length of string in strs
        for s in strs:
            min_length = min(min_length, len(s))

        # go through all character in min string
        i = 0

        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]

            i += 1

        return strs[0][:min_length]


driver = Solution()
ex1 = ["flower", "flow", "flight"]
ex2 = ["dog", "racecar", "car"]

print(f"Example 1:\Input: strs = {ex1}\nOutput: {driver.longestCommonPrefix(ex1)}\n")
print(f"Example 2:\Input: strs = {ex2}\nOutput: {driver.longestCommonPrefix(ex2)}\n")
