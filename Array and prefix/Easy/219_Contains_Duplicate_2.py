'''219. Contains Duplicate II'''

'''
Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
'''


# Brute force
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        return False

# Time Complexity: O(n^2)

# optimal solution
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_to_index = {}  # Hashmap to store last seen index of each number

        for i in range(len(nums)):
            if nums[i] in num_to_index:
                prev_index = num_to_index[nums[i]]
                if abs(i - prev_index) <= k:
                    return True  # Found duplicate within allowed distance

            # Always update the index for current element
            num_to_index[nums[i]] = i

        return False  # No duplicates found within distance k
#✔ Time Complexity: O(n)