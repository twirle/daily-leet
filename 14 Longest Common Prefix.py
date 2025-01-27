# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string ""

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        result = ''
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return result

            result += strs[0][i]
        return result

    def __init__(self):
        strs = ["flower", "flow", "flight"]
        result = self.longestCommonPrefix(strs)
        print(result)

        # flower
        # flow

        # fl


solution = Solution()
