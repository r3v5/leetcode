from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):

            # 1st base case when new interval is before cur interval
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]

            # 2nd base case when new interval is after cur interval
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])

            # 3rd base case when new interval overlaps cur interval
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]

        result.append(newInterval)

        return result

    # Time: O(n)
    # Space: O(n)
