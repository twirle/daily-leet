# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.

class Solution(object):
    def characterReplacement(self, s, k):
        freq = {}
        left = 0
        longest = 0
        result = 0

        for right in range(len(s)):
            # add / increment from new value from s
            freq[s[right]] = 1 + freq.get(s[right], 0)

            # update current longest
            longest = max(freq[s[right]], longest)

            # check if no. of changes needed > k
            size = right - left + 1

            if size - longest > k:
                # update left
                freq[s[left]] -= 1
                left += 1

        result = max(result, right - left + 1)
        return result

    def __init__(self):
        s = "AABABBA"
        k = 1
        result = self.characterReplacement(s, k)
        print(result)

        # time complex: o(n)
        # space complex: o(m), m is the number of unique chars

        # can use freq = {} dict or Counter
        # if freq, have to use 1 + freq.get()
        # if counter, can just += 1


solution = Solution()
