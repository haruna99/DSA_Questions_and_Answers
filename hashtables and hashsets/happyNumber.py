'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
'''

################# Time: O(logn)  Space: O(1) #####################
class Solution:
    def isHappy(self, n: int) -> bool:
        
        if n == 1:
            return True
        def get_sum(n):
            total = 0
            while n > 0:
                total += (n % 10)**2
                n = n // 10
                
            return total
        slow = n
        fast = get_sum(n)
        while slow != fast:
            if slow == 1 or fast == 1:
                return True
            slow = get_sum(slow)
            fast = get_sum(get_sum(fast))

        return False
    

################# Time: O(logn)  Space: O(logn) #####################
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}
        
        def check(val):
            if val == 1:
                return True
            total = 0
            while val > 0:
                val, digit = divmod(val, 10)
                total += digit**2
            if total in seen:
                return False
            seen.add(total)

            return check(total)
            
        return check(n)