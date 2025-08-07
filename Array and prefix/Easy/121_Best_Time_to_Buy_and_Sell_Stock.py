'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock 
and choosing a different day in the future to sell that stock.
'''

# Brute force
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        n = len(prices)

        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)

        return max_profit
# time complexity is (Brute Force – O(n²))



# optimal solution
class Solution:
    def max_profit(self, prices):
        l, r = 0, 1  # left = buy, right = sell
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r  
            r += 1  

        return max_profit



# Both are equally efficient in performance, but for clarity and maintainability, 
# the min-tracking version is generally preferred:
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit

