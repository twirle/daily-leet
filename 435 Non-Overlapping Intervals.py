# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.


# Example 1:
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

# Example 2:
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

# Example 3:
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort()
        # initialise counter
        overlaps = 0
        previous = intervals[0][1]

        for interval in intervals[1:]:
            # if not overlapping:
            # previous interval ends before current interval starts
            # then we don't have to remove an interval and we 'join' the two intervals
            if previous <= interval[0]:
                previous = interval[1]

            # if there is an overlap
            else:
                overlaps += 1
                previous = min(interval[1], previous)

        return overlaps

    def __init__(self):
        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        result = self.eraseOverlapIntervals(intervals)
        print(result)

        # 1 - 2
        # 2 - 3
        # 3 - 4
        # 1 - 3

        # overlap: interval[-1][1] <= interval[0]
        # therefore if interval[-1][1] > interval[0], it is an overlap

        # check if the end of left interval is < start of right interval
        # 2 - 4 < 3 - 5 : overlapping interval

        # check if there's interval within another interval
        # 2 - 3 is inside 2 - 4

        # if there is a interval that is bigger than the smaller one, we should delete the larger one so we have less overlaps


solution = Solution()
