class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # base case
        if len(s) > len(t):
            return False

        if len(s) == 0:
            return True

        # a b c
        # l

        # a h b g d c
        # r

        l = 0

        for r in range(len(t)):
            if s[l] == t[r]:

                # check if we reached the end of the string
                if l == len(s) - 1:
                    return True

                l += 1

        return False


ex_1_s = "abc"
ex_1_t = "ahbgdc"
ex_2_s = "axc"
ex_2_t = "ahbgdc"

driver = Solution()
print(
    f"Example 1:\nInput: s = {ex_1_s}, t = {ex_1_t}\nOutput: {driver.isSubsequence(ex_1_s, ex_1_t)}\n"
)
print(
    f"Example 2:\nInput: s = {ex_2_s}, t = {ex_2_t}\nOutput: {driver.isSubsequence(ex_2_s, ex_2_t)}\n"
)
