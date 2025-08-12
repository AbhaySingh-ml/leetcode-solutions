'''53. Maximum Subarray'''
'''Given an integer array nums, find the subarray with the largest sum, and return its sum.'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n
            max_sum = max(max_sum, curr_sum)
        return max_sum




# 📌 Highlights of the Code
# Robustness: Includes an edge-case check for empty lists.
# Clarity: Clear variable names (curr_sum, max_sum) and inline comments.
# Efficiency: Runs in O(n) time and O(1) space.
# Type Safety: Uses typing.List[int] and return type annotation.
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            raise ValueError("Input list 'nums' must not be empty.")

        max_sum = curr_sum = nums[0]

        for num in nums[1:]:
            # Either extend the current subarray or start a new one at num
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum

