class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")": "(", "}": "{", "]": "["}
        stack = []

        for i in range(len(s)):
            if s[i] not in hashmap:
                stack.append(s[i])

            elif s[i] in hashmap:
                if not stack:
                    return False

                else:
                    open_bracket = stack.pop()
                    if hashmap[s[i]] != open_bracket:
                        return False

        return not stack


ex_1 = "()"
ex_2 = "()[]{}"
ex_3 = "(]"

driver = Solution()
print(f"Example 1:\nInput: s = {ex_1}\nOutput: {driver.isValid(ex_1)}\n")
print(f"Example 2:\nInput: s = {ex_2}\nOutput: {driver.isValid(ex_2)}\n")
print(f"Example 3:\nInput: s = {ex_3}\nOutput: {driver.isValid(ex_3)}\n")
