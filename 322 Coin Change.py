# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:

# Input: coins = [2], amount = 3
# Output: -1

# Example 3:

# Input: coins = [1], amount = 0
# Output: 0


# given [1, 2, 5]
# dp[0] = 0
# dp[1] = 1
# dp[2] = 1
# dp[3] = 1 + dp[1] = 2; 1 + dp[2] = 1 + 1 = 2
# dp[4] = 1 + dp[4-1] = 3; 1 + dp[4-2] = 2
# dp[5] = 1
# dp[6] = 1 + dp[6-1] = 2; 1+ dp[6-2] = 3; 1 + dp[6-5] = 2
# dp[7] = 1 + dp[7-1] = 3; 1 + dp[7-2] = 2; 1 + dp[7-5] = 2

class Solution(object):
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        # initialise array amount + 1 slots of max amounts, [12, 12, ..., 12]
        dp[0] = 0

        for amount in range(1, amount + 1):
            # 1 - 12 since amount = 11
            for coin in coins:
                # 1, 2, 5
                if amount - coin >= 0:
                    dp[amount] = min(dp[amount], 1 + dp[amount - coin])

        if dp[amount] != amount + 1:
            return dp[amount]
        else:
            return -1

    def __init__(self) -> None:
        coins = [1, 2, 5]
        amount = 11
        result = self.coinChange(coins, amount)
        print(result)


solution = Solution()
