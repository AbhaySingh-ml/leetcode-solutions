'''229. Majority Element II'''
'''Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.'''

# using code of part 1 problem
# HashMap (dictionary) method
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, maxCount = 0, 0

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxCount else res
            maxCount = max(count[n], maxCount)

        return res
    
# solution of part 2
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        res = []
        n = len(nums)

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, freq in count.items():
            if freq > n // 3:
                res.append(num)

        return res
    

# another solution of leetcode 
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1, c2, v1, v2 = 0, 1, 0, 0
        for num in nums:
            if num == c1:
                v1 += 1
            elif num == c2:
                v2 += 1
            elif v1 == 0:
                c1, v1 = num, 1
            elif v2 == 0:
                c2, v2 = num, 1
            else:
                v1 -= 1
                v2 -= 1

        cnt1 = cnt2 = 0
        for num in nums:
            if num == c1:
                cnt1 += 1
            elif num == c2:
                cnt2 += 1

        res = []
        if cnt1 > len(nums) // 3:
            res.append(c1)
        if cnt2 > len(nums) // 3:
            res.append(c2)
        return res

