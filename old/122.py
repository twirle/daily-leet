class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost = 0
        best = 0
        if len(prices) == 0:
            return 0
        minPrice = prices[0]
        for i in range(len(prices)):
            cost = prices[i]
            minPrice = min(minPrice, prices[i])
            cost = prices[i] - minPrice
            best = max(best, cost)
        return best

        class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sales = 0
        minPrice = prices[0]
        if len(prices) == 0:
            return 0
        for i in range(1, len(prices)-1):
            minPrice = min(minPrice, prices[i])
            if prices[i+1] < prices[i]:
                sales += prices[i] - minPrice
                minPrice = prices[i+1]
        if sales == 0:
            sales += max(prices) - minPrice 
        return sales
