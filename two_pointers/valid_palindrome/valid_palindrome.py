class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:

            if not s[l].isalnum():
                l += 1

            elif not s[r].isalnum():
                r -= 1

            elif s[l].lower() != s[r].lower():
                return False

            else:
                l += 1
                r -= 1

        return True

    # Time Complexity: O(n)


ex_1 = "A man, a plan, a canal: Panama"
ex_2 = "race a car"
ex_3 = " "

driver = Solution()
print(f"Example 1:\nInput: s = {ex_1}\nOutput: {driver.isPalindrome(ex_1)}\n")
print(f"Example 2:\nInput: s = {ex_2}\nOutput: {driver.isPalindrome(ex_2)}\n")
print(f"Example 3:\nInput: s = {ex_3}\nOutput: {driver.isPalindrome(ex_3)}\n")
