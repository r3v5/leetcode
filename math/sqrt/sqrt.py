class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        result = 0

        while l <= r:
            mid = (l + r) // 2

            if mid**2 < x:
                l = mid + 1
                result = mid

            elif (mid**2) > x:
                r = mid - 1

            else:
                return mid

        return result

    # Time: O(logn)
    # Space: O(1)
