'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        seen = {}

        i = 0
        j = 0

        while j < len(nums):
            if j-i > k:
                del seen[nums[i]]
                i += 1
            if nums[j] in seen:
                return True

            seen[nums[j]] = True

            j += 1

        return False
        