# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

#     -1: Your guess is higher than the number I picked (i.e. num > pick).
#     1: Your guess is lower than the number I picked (i.e. num < pick).
#     0: your guess is equal to the number I picked (i.e. num == pick).

# Return the number that I picked.

# Example 1:
# Input: n = 10, pick = 6
# Output: 6

# Example 2:
# Input: n = 1, pick = 1
# Output: 1

# Example 3:
# Input: n = 2, pick = 1
# Output: 1


class Solution(object):
    def guessNumber(self, n):
        left = 1
        right = n

        while True:
            mid = (left + right) // 2
            result = guess(mid)
            # number < target
            if result > 0:
                left = mid + 1

                # number > target
            elif result < 0:
                right = mid - 1

            else:
                return mid