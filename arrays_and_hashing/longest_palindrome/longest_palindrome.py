class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        found_odd_freq = False
        result = 0

        for i in range(len(s)):
            hashmap[s[i]] = 1 + hashmap.get(s[i], 0)

        for freq in hashmap.values():

            # if even freq, add to result
            if freq % 2 == 0:
                result += freq

            else:
                # add freq - 1 to result, since if we have z -> 3, we can take only 2 z's
                result += freq - 1
                found_odd_freq = True

        # if we found odd freq, we can take 1 char for palindrome
        if found_odd_freq:
            result += 1

        return result


ex1 = "abccccdd"
ex2 = "a"
ex3 = "abccccddzzzeeeee"
driver = Solution()

print(f"Example 1:\nInput: {ex1}\nOutput: {driver.longestPalindrome(ex1)}\n")
print(f"Example 2:\nInput: {ex2}\nOutput: {driver.longestPalindrome(ex2)}\n")
print(f"Example 3:\nInput: {ex3}\nOutput: {driver.longestPalindrome(ex3)}\n")
