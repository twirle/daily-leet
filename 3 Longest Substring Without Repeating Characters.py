# Given a string s, find the length of the longest
# substring
# without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # stores last seen index of chars
        # left = start of current string
        hashMap = {}
        left = 0
        result = 0

        for right in range(len(s)):
            if s[right] in hashMap:
                # update left to avoid repeat char
                left = max(hashMap[s[right]] + 1, left)

            # store last seen index of char
            hashMap[s[right]] = right

            # compare longest with new string
            result = max(result, right - left + 1)

        return result

    def __init__(self):
        s = "abcabcbb"
        result = self.lengthOfLongestSubstring(s)
        print(result)

        # tiem complex: o(n)
        # space complex: o(m), where m is the number of unique characters to store in the hash


solution = Solution()
