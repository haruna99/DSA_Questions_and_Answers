'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
'''

#################### Time: O(logn)  Space: O(1) #####################
class Solution:
    def search(self, nums, target: int) -> int:

        if len(nums) == 1 and target in nums:
            return 0

        left = 0
        right = len(nums)-1
        mid = left + (right-left)//2
            
        while left <= right:
            mid = left + (right-left)//2
            if mid == 0 or mid == len(nums)-1 or nums[mid] > nums[mid+1]:
                break
            if nums[mid] < nums[mid-1]:
                mid -= 1
                break
                    
            if nums[mid] > nums[-1]:
                left = mid+1
            elif nums[mid] < nums[-1]:
                right = mid-1

        second = self.get_num(nums,target,mid+1, len(nums)-1)
        first = self.get_num(nums,target,0, mid+1)

        if first is not None:
            return first
        if second is not None:
            return second
        return -1
        

    def get_num(self, lst, target, left, right):
        if left >= 0 and right < len(lst):
            while left <= right:
                mid = left + (right-left)//2
                
                if lst[mid]==target:
                    return mid
                elif lst[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
        return None

        
################## Time: O(n)  Space: O(1) ####################
class Solution1:
    def search(self, nums, target: int) -> int:
        
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        return -1