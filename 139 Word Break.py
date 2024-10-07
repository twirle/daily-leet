# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false

class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= len(s) and s[i: i + len(word)] == word:
                    # if the word fits within the last few slots of s,
                    # applepen apple and there's 'apple'
                    # this is at i = 8, len(word) = 5 from 'apple'

                    # then also for s[i:i + len(word)]
                    # for i = 8, to i+ len(word), which is 5, if for i = 8 to i = 13 == word
                    # so if the applepen'apple' is the same as 'apple'
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    print(i, dp[i])
                    break
        return dp[0]

    def __init__(self) -> None:
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        result = self.wordBreak(s, wordDict)
        print(result)


solution = Solution()
