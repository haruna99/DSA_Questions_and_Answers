'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
'''

######################### Time: O(n)  Space: O(1) #############################
class Solution:
    def longestOnes(self, nums, k: int) -> int:
        
        i = 0
        zeros = 0
        maximum = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zeros += 1
            if zeros > k:
                
                if nums[i] == 0:
                    zeros -= 1
                i += 1
            if zeros <= k:
                maximum = max(maximum, j-i+1)
        return maximum

#################### Time: O(n2) #Space: O(n) ###############################
class Solution1:
    def longestOnes(self, nums, k: int) -> int:
        
        i = 0
        zero_index = {}
        maximum = 0
        for j in range(len(nums)):
            if nums[j] == 0:
               zero_index[j] = True
            if len(zero_index) > k:
                
                i = min(zero_index) +1
                del zero_index[min(zero_index)]

            maximum = max(maximum, j-i+1)


        return maximum
for i in range(-1,-5,-1):
    print(i)