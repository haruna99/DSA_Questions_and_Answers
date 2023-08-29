'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

'''


######################### two pointer approach ###############################
class Solution:
    def moveZeroes(self, nums) -> None:
        
        fast, slow = 0,-1
        n = len(nums)
        while fast < n:
            if nums[fast] != 0:
                slow += 1
                nums[slow] = nums[fast]

            fast += 1
        for i in range(slow+1, n):
            nums[i]=0


class Solution1:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        n = len(nums)
        count = 0
        zeros = 0
        for i in range(n):
            if nums[i] != 0:
                nums.append(nums[i])
                count += 1
            else:
                zeros += 1
        for i in range(count):
            nums[i] = nums[len(nums)-count+i]
        
        for _ in range(count):
            nums.pop()
        for i in range(zeros):
            nums[len(nums)-zeros+i] = 0

        