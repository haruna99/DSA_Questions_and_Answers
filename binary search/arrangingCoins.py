'''
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

 

Example 1:


Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:


Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
'''



import math
############################ Time: O(1)  Space: O(1) ###########################
class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        return int((-1+math.sqrt(1+8*n))/2)


############################ Time: O(n)  Space: O(1) ###########################
class Solution1:
    def arrangeCoins(self, n: int) -> int:
        result = 0

        for i in range(1,n+1):
            n -= i
            if n >= 0:
                result += 1
            else:
                break
        return result

