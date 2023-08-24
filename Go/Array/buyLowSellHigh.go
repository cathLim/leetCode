//https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
//Best time to Buy and Sell Stock
//Condition: Buy low, sell high
func maxProfit(prices []int) int {

    //check content of prices
    length := len(prices)

    switch length{
        case 0,1://no prices or only one price
            return 0
    }

   //if more than one prices, initialise
   //min and max to the first prices
   //maxP which is the maximum profix to 0
    min, max, maxP := prices[0], prices[0], 0

    //loop thru the slices starting from second prices (index 1)
    for _, price := range prices[1:]{
        if price < min {
            min = price
            continue
        }

        if price > max {
            max = price
        }

        profit := price - min
        if profit > maxP{
            maxP = profit
        }
    }
    return maxP
}