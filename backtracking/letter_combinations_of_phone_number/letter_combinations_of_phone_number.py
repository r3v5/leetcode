from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        hashmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []
        stack = [["", 0]]  # combination, index

        while stack:
            combination, index = stack.pop()

            if len(combination) == len(digits):
                result.append(combination)

            else:
                for char in hashmap[digits[index]]:
                    stack.append([combination + char, index + 1])

        return result


ex_1 = "23"
ex_2 = ""
ex_3 = "2"

driver = Solution()
print(
    f"Exampple 1:\nInput: digits = {ex_1}\nOutput: {driver.letterCombinations(ex_1)}\n"
)
print(
    f"Exampple 2:\nInput: digits = {ex_2}\nOutput: {driver.letterCombinations(ex_2)}\n"
)
print(
    f"Exampple 3:\nInput: digits = {ex_3}\nOutput: {driver.letterCombinations(ex_3)}\n"
)
