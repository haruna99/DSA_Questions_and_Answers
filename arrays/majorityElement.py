'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

############## Time: O(n)  Space: O(1) #################
class Solution:
    def majorityElement(self, nums) -> int:
        count = 1
        current = nums[0]

        for num in nums[1:]:
            if count == 0:
                current = num
            if current == num:
                count += 1
            else:
                count -= 1

        return current


############### Time: O(n) Space: O(n) ###############
class Solution1:
    def majorityElement(self, nums) -> int:
        my_dict = {}
        for num in nums:
            if num in my_dict:
                my_dict[num]+= 1
            else:
                my_dict[num] = 1

            if my_dict[num] > len(nums)/2:
                return num


############# Time: O(nlogn) Space: O(n) ##################
class Solution2:
    def majorityElement(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        nums.sort()
        count = 1
        curr = nums[0]
        for num in nums[1:]:
            if num == curr:
                count += 1
            else:
                curr = num
                count = 1
            if count > n/2:
                return num

        
        
