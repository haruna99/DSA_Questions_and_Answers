'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 
'''

############### Time: O(n)  Space: O(1) ####################
class Solution:
    def missingNumber(self, nums) -> int:
        
        n = len(nums)
        total = sum(nums)
        n_total = int(n*(n+1)/2)
        return n_total - total

############### Time: O(n)  Space: O(1) ####################
class Solution1:
    def missingNumber(self, nums) -> int:       
        
        n = len(nums)
        for i in range(n):
            nums[i] += 1

        for i in range(n):
            if abs(nums[i]) < n+1:
                nums[abs(nums[i])-1] = abs(nums[abs(nums[i])-1]) * -1

        for i in range(n):
            if nums[i] >= 0:
                return i
        
        return n
