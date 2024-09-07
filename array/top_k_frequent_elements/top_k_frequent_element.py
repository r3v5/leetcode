import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums) + 1)]
        hashmap = {}
        result = []

        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)

        for val, freq in hashmap.items():
            arr[freq].append(val)

        counter = 0
        for cell in range(len(arr) - 1, 0, -1):
            for val in arr[cell]:
                result.append(val)
                counter += 1

                if counter == k:
                    return result


"""
               i
Input: nums = [1, 1, 1, 2, 2, 3], k = 2

                                          cell
        arr = [[], [3], [2], [1], [], [], []]
               0    1   2   3      4   5   6
max heap

        (freq, val)
           -3, 1
        -2, 2  -1, 3 


HASHMAP
1: 3
2: 2
3: 1


Time: O(n)
Space: O(n)

Output: [1,2]
"""
