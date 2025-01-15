# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

# Example 1:
# Input: intervals = [(0,40),(5,10),(15,20)]
# Output: 2

# Explanation:
# day1: (0,40)
# day2: (5,10),(15,20)

# Example 2:
# Input: intervals = [(4,9)]
# Output: 1
# Note:
# (0,8),(8,10) is not considered a conflict at 8


class Solution(object):
    def minMeetingRooms(self, intervals) -> int:
        intervals.sort()
        days = 0
        previous = intervals[0][1]

        # iterate through intervals

        for interval in intervals[1:]:
            # check if next interval starts after the previous interval ends
            if previous < interval[0]:
                previous = interval[1]
                # if interval ends before next one starts, it still is part of the same day, append the interval to the list
            else:
                # if interval doesn't end before next one starts, increment day counter
                # set current interval to be previous
                days += 1
                previous = max(previous, interval[1])

        return days

    # alternative way using 2 pointer
    def minMeetingRooms2(self, intervals):
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]

        result, count = 0, 0
        st, en = 0, 0

        while st < len(intervals):
            # if meeting starts before meeting ends, there is +1 ongoing meeting
            if start[st] < end[en]:
                st += 1
                count += 1

            # start[st] > end[end]
            # meeting starts after meeting ends
            else:
                en += 1
                count -= 1
            result = max(count, result)
        return result

    def __init__(self):
        intervals = [(0, 40), (5, 10), (15, 20)]
        # intervals = [(4, 9)]

        result = self.minMeetingRooms2(intervals)
        print(result)

        # (0, 40)
        # (5, 10), (15, 20)

        # time complex: O(n log n)
        # space complex: O(n)


solution = Solution()
