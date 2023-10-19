'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

 

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1
 
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        s1 = []
        s2 = []
        
        while x > 0:
            digit = x % 2
            s1.append(digit)
            x = x//2
        while y > 0:
            digit = y % 2
            s2.append(digit)
            y = y//2
        while len(s1) < len(s2):
            s1.append(0)
        while len(s2) < len(s1):
            s2.append(0)
            
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1

        return count