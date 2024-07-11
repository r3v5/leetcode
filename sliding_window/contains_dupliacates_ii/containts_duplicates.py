from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1

            if nums[r] in window:
                return True

            window.add(nums[r])

        return False

    # Time Complexity: O(n)


ex_1 = [1, 2, 3, 1]
ex_1_k = 3

ex_2 = [1, 0, 1, 1]
ex_2_k = 1

ex_3 = [1, 2, 3, 1, 2, 3]
ex_3_k = 2

driver = Solution()

print(
    f"Example 1:\nInput: nums = [1,2,3,1], k = 3\nOutput: {driver.containsNearbyDuplicate(ex_1, ex_1_k)}\n"
)
print(
    f"Example 2:\nInput: nums = [1,0,1,1], k = 1\nOutput: {driver.containsNearbyDuplicate(ex_2, ex_2_k)}\n"
)
print(
    f"Example 3:\nInput: nums = [1,2,3,1,2,3], k = 2\nOutput: {driver.containsNearbyDuplicate(ex_3, ex_3_k)}\n"
)
