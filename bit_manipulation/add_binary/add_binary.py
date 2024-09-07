class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        a = a[::-1]
        b = b[::-1]
        length = max(len(a), len(b))

        for i in range(length):
            if i < len(a):
                digit_a = int(a[i])

            else:
                digit_a = 0

            if i < len(b):
                digit_b = int(b[i])

            else:
                digit_b = 0

            summ = digit_a + digit_b + carry
            digit_to_add = str(summ % 2)
            result = digit_to_add + result
            carry = summ // 2

        if carry:
            result = str(carry) + result

        return result


"""
        a = "11", b = "1"

        carry = 1
        result = ""
        a = a[::-1]
        b = b[::-1]

                11
               +01
               ___
                00

        summ = 1 + 1 + carry = 2
        digit = summ % 2 = 0   
        carry = summ // 2 = 1

        if carry:
            result = str(carry) + result

Time: O(n + m)
Space: O(1)
"""
