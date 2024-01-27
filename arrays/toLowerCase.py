'''
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 

Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"
 

Constraints:

1 <= s.length <= 100
s consists of printable ASCII characters.
'''

class Solution(object):
    def toLowerCase(self, s):
        ################################ Time: O(n) Space: O(n) #########################
        result = []
        for letter in s:
            n_letter = ord(letter)
            
            if n_letter >=65 and n_letter <= 90:
                val = ord(letter) + 32
                result.append(chr(val))
            else:
                result.append(letter)

        return "".join(result)