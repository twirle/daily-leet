# You are given an array nums consisting of positive integers.
# We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.
# Return the length of the longest nice subarray.
# A subarray is a contiguous part of an array.
# Note that subarrays of length 1 are always considered nice.

# Example 1:
# Input: nums = [1,3,8,48,10]
# Output: 3
# Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
# - 3 AND 8 = 0.
# - 3 AND 48 = 0.
# - 8 AND 48 = 0.
# It can be proven that no longer nice subarray can be obtained, so we return 3.

# Example 2:
# Input: nums = [3,1,5,11,13]
# Output: 1
# Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.


class Solution(object):
    def longestNiceSubarray(self, nums):
        length = 0
        left = 0
        current = 0

        # use two pointer to
        for right in range(len(nums)):
            while current & nums[right]:
                # unset the bits from left pointer
                current = current ^ nums[left]
                left += 1
            # check longest length
            length = max(right - left + 1, length)

            # set with current right pinter
            current = current ^ nums[right]

        return length

    def __init__(self):
        nums = [1, 3, 8, 48, 10]
        result = self.longestNiceSubarray(nums)
        print(result)

    #               current
    # 1 | 000001    000001
    # 3 | 000011    000011  add 3
    # 8 | 001000    001011  add 8
    # 48| 110000    111011  add 48
    # 10| 001010    111011 & 10 != 0
    #               111010  removed 1 != 0
    #               111000  removed 3 != 0
    #               110000  removed 8 != 0
    #               111010  add 10


solution = Solution()
