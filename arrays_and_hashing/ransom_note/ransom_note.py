class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ransom_note = [0] * 26
        count_magazine = [0] * 26

        for i in range(len(ransomNote)):
            count_ransom_note[ord(ransomNote[i]) - ord("a")] += 1

        for i in range(len(magazine)):
            count_magazine[ord(magazine[i]) - ord("a")] += 1

        for i in range(26):
            if count_ransom_note[i] > count_magazine[i]:
                return False

        return True


driver = Solution()
ex1_ransom_note = "a"
ex1_magazine = "b"

ex2_ransom_note = "aa"
ex2_magazine = "ab"

ex3_ransom_note = "aa"
ex3_magazine = "aab"

print(
    f"Example 1:\nInput: ransomNote = {ex1_ransom_note}, magazine = {ex1_magazine}\nOutput: {driver.canConstruct(ex1_ransom_note, ex1_magazine)}\n"
)
print(
    f"Example 2:\nInput: ransomNote = {ex2_ransom_note}, magazine = {ex2_magazine}\nOutput: {driver.canConstruct(ex2_ransom_note, ex2_magazine)}\n"
)
print(
    f"Example 3:\nInput: ransomNote = {ex3_ransom_note}, magazine = {ex3_magazine}\nOutput: {driver.canConstruct(ex3_ransom_note, ex3_magazine)}\n"
)
