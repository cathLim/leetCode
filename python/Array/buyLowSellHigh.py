#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#Best Time to Buy and Sell Stock
#Condition: Buy low, sell high
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1 
        maxP = 0

        while sell < len(prices):
            #check profitable?
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxP = max(maxP, profit)
            else:
                buy = sell
            sell+=1
        return maxP
