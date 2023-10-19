'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''


class Solution:
    def fourSum(self, nums, target: int):
        nums = sorted(nums)
        n = len(nums)
        result = []
        for i in range(n-3):
            if i == 0 or nums[i] != nums[i-1]:
                for j in range(i+1, n-2):
                    if nums[j] != nums[j-1] or j-1 == i:
                        seen = set()
                        seen3 = set()
                        for k in range(j+1,n):
                            if nums[k] in seen3:
                                continue
                            
                            complement = target - nums[i]-nums[j]-nums[k]
                            
                            if complement in seen:
                                result.append([nums[i], nums[j], nums[k], complement])
                                seen3.add(nums[k])
                            else:
                                seen.add(nums[k])
        return result

        