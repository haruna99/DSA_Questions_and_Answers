'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        result = 0
        new_max = 0
        for num in nums:
            if num == 1:
                new_max +=1
            else:
                result = max(result, new_max)
                new_max = 0

        return max(result, new_max)