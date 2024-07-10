import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        # use max heap
        max_heap = []
        hashmap = {}
        result = ""

        for i in range(len(s)):
            hashmap[s[i]] = 1 + hashmap.get(s[i], 0)

        for char, freq in hashmap.items():
            max_heap.append([-1 * freq, char])

        heapq.heapify(max_heap)

        while max_heap:
            freq, char = heapq.heappop(max_heap)
            freq *= -1
            result += char * freq

        return result

    # Time Complexity: O(nlogn)


ex_1 = "tree"
ex_2 = "cccaaa"
ex_3 = "Aabb"

driver = Solution()
print(f"Example 1:\nInput: s = {ex_1}\nOutput: {driver.frequencySort(ex_1)}\n")
print(f"Example 2:\nInput: s = {ex_2}\nOutput: {driver.frequencySort(ex_2)}\n")
print(f"Example 3:\nInput: s = {ex_3}\nOutput: {driver.frequencySort(ex_3)}\n")
