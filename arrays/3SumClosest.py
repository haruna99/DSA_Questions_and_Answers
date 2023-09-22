'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 
'''

class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        hash_set = set()
        remainder = float("inf")
        result = 0
        for i in range(len(nums)-2):
            if nums[i] not in hash_set:
                j = i+1
                k = len(nums)-1
                while j < k:
                    new_sum = nums[i]+nums[j]+nums[k]
                    new_remainder = abs(target-new_sum)
                    if new_remainder < remainder:
                        remainder = new_remainder
                        result = new_sum
                    if target-new_sum > 0:
                        j += 1
                    elif target-new_sum < 0:
                        k -= 1
                    else:
                        return result
                    
            hash_set.add(nums[i])
        return result