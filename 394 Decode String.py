# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"

# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

class Solution(object):
    def decodeString(self, s):
        stack = []
        multiply = []
        chars = ''
        x = 0

        for char in s:
            if char.isdigit():
                x = x * 10 + int(char)

            elif char == '[':
                stack.append(chars)
                multiply.append(x)
                chars = ''
                x = 0

            elif char == ']':
                temp = chars
                chars = stack.pop()
                multiplier = multiply.pop()
                chars += temp * multiplier

            else:
                chars += char

        return chars

    def __init__(self):
        # s = "2[abc]3[cd]ef"
        s = "3[a2[c]]"
        result = self.decodeString(s)
        print(result)

        # multiply = [3]
        # stack = ['']
        # characters = acc
        # x = 0

        # time complex: 0(n)
        # space complex: 0(n)


solution = Solution()
