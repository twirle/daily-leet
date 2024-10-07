def maxProfit(prices):
    bestbuy = -prices[0]
    nextbuy = 0
    profit = 0
    fullprofit = 0
    if len(prices) == 0:
        return 0
    
    for price in prices:
        bestbuy = max(bestbuy, -price)
        profit = max(profit, price + bestbuy)
        nextbuy = max(nextbuy, profit - price)
        fullprofit = max(fullprofit, price + nextbuy)
    
    return fullprofit

prices = [3,3,5,0,0,3,1,4]
print(maxProfit(prices))