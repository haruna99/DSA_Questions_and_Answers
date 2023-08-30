'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''


######################## Time: O(n) Space: O(1) ###########################
class Solution:
    def productExceptSelf(self, nums):

        left_product = 1
        answer =[None]*len(nums)

        for i in range(len(nums)):
            if i == 0:
                answer[i] = 1
            else:
                left_product *= nums[i-1]
                answer[i] = left_product

        right_product = 1
        for i in range(len(nums)-1,-1,-1):
            if i != len(nums)-1:
                right_product *= nums[i+1]
                answer[i] *= right_product

        return answer

######################## Time: O(n) Space: O(n) ###########################
class Solution1:
    def productExceptSelf(self, nums):
        zeros = {}
        product = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros[i] = True
            else:
                product*= nums[i]

        answer = [None]*len(nums)
        for i in range(len(nums)):
            if i in zeros and len(zeros)>1:
                answer[i] = 0
            if i in zeros and len(zeros) == 1:
                answer[i] = product
            if i not in zeros and len(zeros) >0:
                answer[i] = 0
            if i not in zeros and len(zeros) == 0:
                answer[i] = int(product/nums[i])

        return answer