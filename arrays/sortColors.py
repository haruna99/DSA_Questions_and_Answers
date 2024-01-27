'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
'''


class Solution(object):
    def sortColors(self, nums):
        seen = {0:0, 1:0, 2:0}

        for num in nums:
            if num == 0:
                seen[0] += 1
            elif num == 1:
                seen[1] +=1
            else:
                seen[2] += 1

        nums[0:seen[0]] = [0]*seen[0]
        nums[seen[0]:seen[0]+seen[1]] = [1]*seen[1]
        nums[seen[0]+seen[1]:] = [2]*seen[2]

class Solution(object):
    def sortColors(self, nums):
        ################## Time: O(n) Space: O(1) #################
        n = len(nums)
        p0 = 0
        p2 = n-1
        i = 0

        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            else:
                i += 1

        


