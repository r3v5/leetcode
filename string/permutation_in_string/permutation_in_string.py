class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # base case
        if len(s1) > len(s2):
            return False

        count_s1 = [0] * 26
        count_s2 = [0] * 26

        # count chars in s1 and build up an initial window for s2
        # ab -> [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # ei -> [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord("a")] += 1
            count_s2[ord(s2[i]) - ord("a")] += 1

        # check if initial sliding window is equal to s1
        if count_s1 == count_s2:
            return True

        # start sliding window from the end of initial sliding window since we already checked first window
        for i in range(len(s1), len(s2)):
            count_s2[ord(s2[i]) - ord("a")] += 1

            # since we move sliding window we are loosing i - len(s1) char
            # ab
            # ei -> id
            # 0     12
            count_s2[ord(s2[i - len(s1)]) - ord("a")] -= 1

            if count_s1 == count_s2:
                return True

        return False

        # Time Complexity: O(n)


ex1_s1 = "ab"
ex1_s2 = "eidbaooo"

ex2_s1 = "ab"
ex2_s2 = "eidboaoo"

driver = Solution()

print(
    f"Example 1:\nInput: s1 = {ex1_s1}, s2 = {ex1_s2}\nOutput: {driver.checkInclusion(ex1_s1, ex1_s2)}\n"
)
print(
    f"Example 2:\nInput: s1 = {ex2_s1}, s2 = {ex2_s2}\nOutput: {driver.checkInclusion(ex2_s1, ex2_s2)}\n"
)
