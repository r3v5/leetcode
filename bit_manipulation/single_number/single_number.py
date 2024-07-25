from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # make xor operation for each number
        """
        result = 0
        4 - 100       1) 100 ^ 0 = 100
        1 - 001       2) 100 ^ 001 = 101
        2 - 010       3) 101 ^ 010 = 111
        1 - 001       4) 111 ^ 001 = 110
        2 - 010       5) 110 ^ 010 = 100 -> 4
        """
        result = 0

        for num in nums:
            result = num ^ result

        return result

    # Time: O(n)
    # Space: O(1)
