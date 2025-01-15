# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

class Solution(object):
    def longestConsecutive(self, nums):
        # sorting is time complex O(nlog(n)) so thats too big

        numSet = set(nums)
        longest = 0

        for num in nums:
            # check if it starts the consec sequence, if yes then start length = 1
            if (num - 1) not in numSet:
                next_num = num + 1
                length = 1

                # check if the onsecutive sequence continues, if yes then length += 1, until it ends
                while next_num in numSet:
                    length += 1
                    next_num += 1
                longest = max(longest, length)
        return longest

    def __init__(self):
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        result = self.longestConsecutive(nums)
        print(result)


solution = Solution()
