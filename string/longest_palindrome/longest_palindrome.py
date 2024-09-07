class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest = 0
        hashmap = {}
        found_odd_freq = False

        for i in range(len(s)):
            hashmap[s[i]] = 1 + hashmap.get(s[i], 0)

        for freq in hashmap.values():
            if freq % 2 == 0:
                longest += freq

            else:
                longest += freq - 1
                found_odd_freq = True

        if found_odd_freq:
            longest += 1

        return longest


sol = Solution()


def test(s: str, exp: int) -> None:
    assert (
        sol.longestPalindrome(s) == exp
    ), f"exp: {exp}, but got: {sol.longestPalindrome(s)}"


test("abccccdd", 7)
test("a", 1)


"""
        s = "aaabccccdd"

                dccaaaccd

longest = 2 + 0 + 4 + 2 = 8 + 1

HASHMAP 
a: 3
b: 1
c: 4
d: 2

if freq is even:
    longest += freq

else:
    longest = (freq - 1 + longest)


Time: O(n)
Space: O(n)

"""
