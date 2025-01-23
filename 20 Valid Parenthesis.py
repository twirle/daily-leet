# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.


# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

class Solution(object):
    def isValid(self, s):
        stack = []
        hash = {')': '(', ']': '[', '}': '{'}

        for item in s:
            if item in hash:
                if stack and stack[-1] == hash[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)

        if not stack:
            return True
        else:
            return False

    def __init__(self):
        s = "()[]{}"
        result = self.isValid(s)
        print(result)

        # time complex: o(n)
        # space complex: o(n)


solution = Solution()
