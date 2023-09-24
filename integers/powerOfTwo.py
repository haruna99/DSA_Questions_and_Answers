'''
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
'''

###################### Time: O(1)  Space: O(1) ################################
import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n < 1:
            return False
    
        return math.log2(n) % 1 == 0
    
###################### Time: O(logn)  Space: O(1) ################################
class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False

        while n % 2 == 0:
            n = n/2

        return n == 1