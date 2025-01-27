# Given two strings s and t, return true if t is an
# anagram
# of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false


class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        char = {}

        for i in range(len(s)):
            char[s[i]] = char.get(s[i], 0) + 1
            char[t[i]] = char.get(t[i], 0) - 1

            # .get(x, 0) : the 0 is returned if nothing found

        for count in char.values():
            if count != 0:
                return False

        return True

    def __init__(self):
        s = "anagram"
        t = "nagaram"
        result = self.isAnagram(s, t)
        print(result)

        # scan and sort is o(n log n) so no


solution = Solution()
