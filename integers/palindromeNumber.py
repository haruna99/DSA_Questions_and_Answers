'''
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        y = x

        reverted_number = 0
        while y > 0:
            y,remainder = divmod(y,10)
            reverted_number = reverted_number*10 + remainder

        print(x, reverted_number)
        return x == reverted_number
    


class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        string = str(x)
        i = 0
        j = len(string) - 1

        while i<j:
            if string[i] != string[j]:
                return False
            i+=1
            j-=1

        return True