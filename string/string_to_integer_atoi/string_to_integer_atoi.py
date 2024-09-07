class Solution:
    def myAtoi(self, s: str) -> int:
        # Remove leading whitespaces
        s = s.lstrip()

        # Edge case: empty string after trimming
        if not s:
            return 0

        # Initialize variables
        sign = 1
        num = 0
        i = 0

        # Check sign
        if s[0] == "+":
            i += 1
        elif s[0] == "-":
            sign = -1
            i += 1

        # Process digits
        while i < len(s) and s[i].isdigit():
            num = 10 * num + int(s[i])
            i += 1

        num *= sign

        if num < (-(2**31)):
            return -(2**31)

        elif num > (2**31 - 1):
            return 2**31 - 1

        else:
            return num


"""
1. base case: if not s return None

steps:
1. remove whitespaces using lstrip()
2. check sign:
    if s[0] == "-":
        sign = -1
    
    else:
        sign = 1

3. build num
4. apply sign
5. check the range

            01
Input: s = "42"
            i

num = 0
num = 10 * num + int(s[i])

Time: O(n)
Space: O(1)


"""
