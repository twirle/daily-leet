# Given an array of meeting time intervals consisting of stat and end times [[s1, e1]], [s2,e2],...], determine if a person could attend all meetings

# Input: intervals = [(0, 30), (5, 10), (15, 20)]
# Output: false
# Explanation: (0, 30), (5, 10) and (0, 30), (15, 20) will conflict.

class Solution(object):
    # def canAttendMeetings(self, intervals):
    #     intervals.sort()

    #     for i in range(len(intervals) - 1):
    #         interval1 = intervals[i]
    #         interval2 = intervals[i + 1]

    #         if interval1.end > interval2.start:
    #             return False

    #     return True

    def canAttendMeetings(self, intervals):
        intervals.sort()
        previous = intervals[0][1]

        for interval in intervals[1:]:
            if previous < interval[0]:
                previous = interval[1]

            else:
                return False

        return True

    def __init__(self):
        intervals = [(0, 30), (5, 10), (15, 20)]
        result = self.canAttendMeetings(intervals)
        print(result)

        # sort intervals
        # if the first interval ends after the next interval starts, it conflicts


solution = Solution()
