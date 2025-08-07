'''122. Best Time to Buy and Sell Stock II'''

'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

'''

# brute force
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def helper(day: int, holding: bool) -> int:
            # Base case: no more days left
            if day == len(prices):
                return 0

            # Case 1: Do nothing today
            profit_if_idle = helper(day + 1, holding)

            if holding:
                # Case 2: Sell today
                profit_if_sold = prices[day] + helper(day + 1, False)
                return max(profit_if_idle, profit_if_sold)
            else:
                # Case 3: Buy today
                profit_if_bought = -prices[day] + helper(day + 1, True)
                return max(profit_if_idle, profit_if_bought)
        
        # Start on day 0, not holding any stock
        return helper(0, False)

# ❌ Time Complexity: O(2^n)


# optimal 
class Solution:
    def buy_sell(self, prices: list) -> int:
        max_profit = 0
        # Loop through the price list starting from day 1
        for i in range(1, len(prices)):
            # If today's price is greater than yesterday's, there's a profit opportunity
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        
        return max_profit
# ✅ Time Complexity: O(n)

