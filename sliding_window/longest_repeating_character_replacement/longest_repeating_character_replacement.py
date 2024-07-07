class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        count_s = [0] * 26

        for r in range(len(s)):
            count_s[ord(s[r]) - ord("A")] += 1

            while (r - l + 1) - max(count_s) > k:
                count_s[ord(s[l]) - ord("A")] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest


ex1 = "ABAB"
ex1_k = 2

ex2 = "AABABBA"
ex2_k = 1

driver = Solution()

print(
    f"Example 1:\nInput: s = {ex1}, k = {ex1_k}\nOutput: {driver.characterReplacement(ex1, ex1_k)}\n"
)
print(
    f"Example 2:\nInput: s = {ex2}, k = {ex2_k}\nOutput: {driver.characterReplacement(ex2, ex2_k)}\n"
)
