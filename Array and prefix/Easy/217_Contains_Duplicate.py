'''217. Contains Duplicate'''

'''Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.'''

#brute force method
class Solution:
    def containsDuplicate(self, nums):
        n = len(nums) #assgin the element of the array(num) in n
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False
    

#Using a Set (Efficient)
class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


