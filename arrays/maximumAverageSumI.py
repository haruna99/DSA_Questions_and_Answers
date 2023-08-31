'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 
'''

class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        if k == 1:
            return max(nums)
        
        new_sum = sum(nums[0:k])
        max_average = new_sum/k
        i = 1
        j = k
        while j < len(nums):
            new_sum = new_sum - nums[i-1] + nums[j]
            new_average = new_sum/k
            max_average = max(max_average, new_average)
            i += 1
            j += 1
            
        return max_average