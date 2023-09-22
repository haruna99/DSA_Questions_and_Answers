'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 
'''

################## Two Pointerss - Time: O(n)  Space: O(n) ####################
class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

################## Time: O(n)  Space: O(n) ##################
class Solution1:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        n = len(s)
        for i in range(n-1, -1,-1):
            s.append(s[i])

        for i in range(n):
            s[i] = s[n+i]
        
        for i in range(n):
            s.pop()
        