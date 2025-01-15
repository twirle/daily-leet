# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.


# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.


class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        merged = []

        for interval in intervals:
            # overlap if: x[1] >= y[0]
            # interval[-1][1] < interval[0]
            if not merged or merged[-1][1] < interval[0]:
                # if there's nothing in interval, when merged is empty,
                # or no overlap when the last item in merged
                merged.append(interval)
            else:
                # there is an overlap so we merge the start of the two we are merging, and larger end
                merged[-1] = merged[-1][0], max(merged[-1][1], interval[1])

        return merged

    def __init__(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        result = self.merge(intervals)
        print(result)

        # 1 - 3
        # 2 - 6
        # 8 - 10
        # 15 - 18

        # time complex: O(n log n), 1 sort
        # space complex: O(n), to hold the


solution = Solution()
