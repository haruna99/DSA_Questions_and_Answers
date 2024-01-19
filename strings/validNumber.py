'''
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

 

Example 1:

Input: s = "0"
Output: true
Example 2:

Input: s = "e"
Output: false
Example 3:

Input: s = "."
Output: false
 

Constraints:

1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
'''


class Solution(object):
    ################## TIme: O(n) Space: O(1) ########################
    def isNumber(self, s):
        count_num = 0
        count_e = 0
        count_dot = 0
        nums = {"0","1","2","3",'4',"5","6","7","8","9"}
        upper = {chr(x) for x in range(ord('A'), ord('Z')+1)} - {'E'}
        lower = {'a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
        if len(s) == 1 and s[0] not in nums:
            return False
        for i in range(len(s)):
            if s[i] in upper or s[i] in lower:
                return False
            if s[i] in nums:
                
                count_num += 1
                continue
            if s[i] != '+' and s[i] != "-":
                
                
                if s[i] == 'E' or s[i] == 'e':
                    
                    count_e += 1
                    if i == 0 or count_e > 1 or i == len(s)-1 or count_num == 0:
                        return False
                    if s[i-1] not in nums and s[i-1] != '.':
                        
                        return False
                    if i+1 < len(s):
                        if s[i+1] not in nums and s[i+1] != "+" and s[i+1] != '-':
                            return False
                elif s[i] == ".":
                    if count_e > 0:
                        return False
                    count_dot += 1
                    if count_dot > 1:
                        return False
                    if i+1 < len(s):
                        
                        if s[i+1] not in nums and s[i+1]!= 'e' and s[i+1] != 'E':
                            return False
                    
            else:
                if i != 0:
                    if (s[i-1] != 'E' and s[i-1] != 'e') or i == len(s)-1:
                        return False
        if count_num == 0:
            return False
                    
        return True