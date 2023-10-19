'''
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537

'''

####################### Time: O(n)  Space: O(n) #########################
class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n < 3:
            return 1
        a,b,c = 0,1,1
        for _ in range(3, n+1):
            a,b,c = b,c,a+b+c

        return c

####################### Time: O(n)  Space: O(n) #########################
class Solution1:
    def tribonacci(self, n: int) -> int:
        
        result = {
            0:0,
            1:1,
            2:1
        }
        if n in result:
            return result[n]
        
        for i in range(3,n+1):
            result[i] = result[i-1]+result[i-2]+result[i-3]
        return result[n]