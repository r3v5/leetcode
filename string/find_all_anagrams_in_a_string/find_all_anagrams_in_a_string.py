from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # base case
        if len(s) < len(p):
            return None

        result = []
        count_s = [0] * 26
        count_p = [0] * 26

        for i in range(len(p)):
            count_p[ord(p[i]) - ord("a")] += 1
            count_s[ord(s[i]) - ord("a")] += 1

        if count_s == count_p:
            result.append(0)

        for i in range(len(p), len(s)):
            count_s[ord(s[i]) - ord("a")] += 1
            count_s[ord(s[i - len(p)]) - ord("a")] -= 1

            if count_s == count_p:
                result.append(i - len(p) + 1)

        return result

    # Time Complexity: O(s + p)


ex_1_s = "cbaebabacd"
ex_1_p = "abc"
ex_2_s = "abab"
ex_2_p = "ab"

driver = Solution()
print(
    f"Example 1:\nInput s = {ex_1_s}, p = {ex_1_p}\nOutput: {driver.findAnagrams(ex_1_s, ex_1_p)}\n"
)
print(
    f"Example 2:\nInput s = {ex_2_s}, p = {ex_2_p}\nOutput: {driver.findAnagrams(ex_2_s, ex_2_p)}\n"
)
