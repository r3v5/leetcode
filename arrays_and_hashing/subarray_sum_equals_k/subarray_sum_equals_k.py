from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        result = 0
        hashmap = {}  # Prefix Sum hashmap: sum -> occurances

        for i in range(len(nums)):
            cur_sum += nums[i]

            if cur_sum == k:
                result += 1

            # find pre calculated prefix sum to cut it and chek if the number equals to k
            # assuming k = 3
            # (1) (2) (3) (1 + 2 + 3 = 6) => 6 - 3 = (3) and (3) == k
            #        |
            # (1) (2) => (1 + 2 = 3)
            if (cur_sum - k) in hashmap:
                result += hashmap[cur_sum - k]

            if cur_sum in hashmap:
                hashmap[cur_sum] += 1

            else:
                hashmap[cur_sum] = 1

        return result


ex_1 = [1, 1, 1]
ex_1_k = 2
ex_2 = [1, 2, 3]
ex_2_k = 3

driver = Solution()
print(
    f"Example 1:\nInput: nums = {ex_1}, k = {ex_1_k}\nOutput: {driver.subarraySum(ex_1, ex_1_k)}\n"
)
print(
    f"Example 2:\nInput: nums = {ex_2}, k = {ex_2_k}\nOutput: {driver.subarraySum(ex_2, ex_2_k)}\n"
)
