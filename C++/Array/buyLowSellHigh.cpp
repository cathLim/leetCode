//https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
//Best time to Buy and Sell Stock
//Condition: Buy low, sell high
class Solution {
public:
    int maxProfit(vector<int>& prices) {

        int buy, profit, maxP = 0;
        if(prices.empty())
        {
            return 0;
        }

        for(int sell=1; sell<prices.size(); sell++)
        {
            if(buy<sell)
            {
                profit = prices[sell] - prices[buy];
                maxP = std::max(maxP, profit);
            }
            else
            {
                buy = sell;
            }
        }
    return maxP;
    }
};