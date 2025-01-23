# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:

# Input: n = 1
# Output: ["()"]

class Solution(object):
    def generateParenthesis(self, n):
        stack = []
        result = []

        def backtrack(open, closed):
            if open == closed == n:
                result.append("".join(stack))
                return

            if open < n:
                stack.append("(")
                backtrack(open + 1, closed)
                stack.pop()
            if open > closed:
                stack.append(")")
                backtrack(open, closed + 1)
                stack.pop()

        backtrack(0, 0)
        return result

    def __init__(self):
        n = 3
        result = self.generateParenthesis(n)
        print(result)

        # like a tree, add open and closed parenthesis
        #        (
        #   ((        ()
        # (((   ())     ()(

        # time complex: o(2**n) as its a tree
        # space complex: o(2n)


solution = Solution()
