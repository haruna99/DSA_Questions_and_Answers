'''
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: 
'''

############### Time: O(n)  Space: O(1) #################
class Solution:
    def firstMissingPositive(self, nums) -> int:
        if 1 not in nums:
            return 1
        
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        for i in range(n):
            nums[abs(nums[i])-1] = abs(nums[abs(nums[i])-1])* -1

        for i in range(n):
            if i >0 and nums[i] > 0:
                return i+1
        return n+1

############### Time: O(n)  Space: O(n) ####################
class Solution1:
    def firstMissingPositive(self, nums) -> int:
        
        my_set = set(nums)

        i = 1
        while True:
            if i not in my_set:
                return i
            i += 1