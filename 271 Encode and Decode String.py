# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:
# Input: ["neet", "code", "love", "you"]
# Output: ["neet", "code", "love", "you"]

# Example 2:
# Input: ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]

class Solution:
    def encode(self, strs):
        result = ''

        for s in strs:
            result += str(len(s)) + '#' + s

        return result

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):
            j = i
            # get length up to #, not just single digit length
            # stop when j = #
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            # i : left, j : right
            i = j + 1
            j = i + length

            result.append(s[i:j])
            i = j

        return result

    def __init__(self):
        strs = ["neet", "code", "love", "you"]
        encode = self.encode(strs)
        print(encode)

        decode = self.decode(encode)
        print(decode)


solution = Solution()
