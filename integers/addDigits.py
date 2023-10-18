'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
'''
################## Time: O(1)  Space: O(1) ###############
class Solution:
    def addDigits(self, num: int) -> int:
        
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9

################### Recursion ###################
class Solution1:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        total = 0
        while num > 0:
            num, digit = divmod(num, 10)
            total += digit

        return self.addDigits(total)


################## Iteration ########################
class Solution2:
    def addDigits(self, num: int) -> int:
        digits_sum = 0

        while num > 0:
            digits_sum += num % 10
            num = num // 10
            if num == 0 and digits_sum > 9:
                num  = digits_sum
                digits_sum = 0
        
        return digits_sum