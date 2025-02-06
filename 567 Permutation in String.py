# Given two strings s1 and s2, return true if s2 contains a
# permutation
# of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

from collections import Counter


class Solution(object):

    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        # check contents of each string and set up sliding window
        s1Count = Counter(s1)
        window = Counter(s2[:len(s1)])

        if s1Count == window:
            return True

        # move the window and check
        for i in range(len(s1), len(s2)):
            # increment character at current index
            window[s2[i]] += 1

            # decrement left-most character (and remove if 0)
            window[s2[i - len(s1)]] -= 1
            if window[s2[i - len(s1)]] == 0:
                del window[s2[i - len(s1)]]

            # check match
            if window == s1Count:
                return True

        return False

    def __init__(self):
        # s1 = "ab"
        # s2 = "eidbaooo"
        s1 = "a"
        s2 = "ab"
        result = self.checkInclusion(s1, s2)
        print(result)

        # time complex: o(n)
        # space complex: o(1)


solution = Solution()
