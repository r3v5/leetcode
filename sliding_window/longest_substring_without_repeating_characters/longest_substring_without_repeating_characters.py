class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        longest = 0
        l = 0

        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)

            while max(hashmap.values()) > 1:
                hashmap[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest

    # Time Complexity: O(n)


ex1 = "abcabcbb"
ex2 = "bbbbb"
ex3 = "pwwkew"

driver = Solution()
print(f"Example 1:\nInput: s = {ex1}\nOutput: {driver.lengthOfLongestSubstring(ex1)}\n")
print(f"Example 2:\nInput: s = {ex2}\nOutput: {driver.lengthOfLongestSubstring(ex2)}\n")
print(f"Example 3:\nInput: s = {ex3}\nOutput: {driver.lengthOfLongestSubstring(ex3)}\n")
