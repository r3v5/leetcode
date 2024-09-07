from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []

        # sort the intervals
        intervals.sort(key=lambda intervals: intervals[0])

        for i in range(len(intervals)):

            # check if not overlapping
            if not result or result[-1][1] < intervals[i][0]:
                result.append([intervals[i][0], intervals[i][1]])

            else:
                # find overlapping intervals -> merge them
                result[-1][0] = min(result[-1][0], intervals[i][0])
                result[-1][1] = max(result[-1][1], intervals[i][1])

        return result

    # Time: O(nlogn)
    # Space: O(n)
