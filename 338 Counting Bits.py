# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Example 2:
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0000    0
# 1 --> 0001    1 + bits(n-1)
# 2 --> 0010    1 + bits(n-2)
# 3 --> 0011    1 + bits(n-2)
# 4 --> 0100    1 + bits(n-4)
# 5 --> 0101    1 + bits(n-4)
# 6 --> 0110    1 + bits(n-4)
# 7 --> 0111    1 + bits(n-4)
# 8 --> 1000    1 + bits(n-8)
# 9 --> 1001    1 + bits(n-8)
# ... until 16 where it will become 1 + bits(n-16)

class Solution(object):
    def countBits(self, n):
        bits = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
                print(offset)
            bits[i] = 1 + bits[i - offset]
        return bits

    def __init__(self) -> None:
        n = 5
        print(self.countBits(n))


solution = Solution()
