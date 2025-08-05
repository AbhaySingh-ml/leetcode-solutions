'''1. Two sum'''

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
# Brute force solution
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if [i] - [j] == target:
                return [i, j]
# ✅ Time Complexity: O(n²)
# Because of the nested loop.

# optimal solution
class Solution:
    def two_sum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i  
# time complexity: O(n)
