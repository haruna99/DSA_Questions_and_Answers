'''
iven an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 
'''
################# Time: O(n)   Space: O(1) ###################
class Solution:
    def increasingTriplet(self, nums) -> bool:
        first = float("inf")
        second = float("inf")

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False

                
################# Time: O(n)  Space: O(n) ########################
class Solution1:
    def increasingTriplet(self, nums) -> bool:
        if len(nums)<=2:
            return False

        prev = []
        minimum = nums[0]
        for i in range(1,len(nums)):
            minimum = min(minimum, nums[i-1])
            prev.append(minimum)

        maximum = nums[len(nums)-1]
        next_list = []
        for i in range(-2,-len(nums)-1,-1):
            maximum = max(maximum, nums[i+1])
            next_list.append(maximum)

        for i in range(1, len(nums)-1):
            if prev[i-1] < nums[i] < next_list[len(nums)-i-1]:
                return True
        return False