"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0"""

def MaxProfit(prices):
    mini_price = float('inf')
    max_profit = 0
    for price in prices:
        mini_price = min(mini_price, price)
        max_profit = max(max_profit, price-mini_price)
    return max_profit

#~~~~~~~Testing~~~~~~~~~~

#Using two pointers

def MaxP_2pointers(prices):
    l, r = 0, 1 #left is for buying, right is for selling 
    max_prof = 0
    while r<len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_prof = max(max_prof, profit)
        else:
            l = r
        r+=1
    return max_prof


prices = [7,6,4,3,1]
prices2 = [7,1,5,3,6,4]
print(MaxProfit(prices))
print(MaxProfit(prices2))
