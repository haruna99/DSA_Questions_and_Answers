'''
Given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.

 

Example 1:

Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
Example 2:

Input: s = "Hello"
Output: 1
'''

class Solution:
    def countSegments(self, s: str) -> int:
        if len(s) == 0:
            return 0
        count = 0
        i = 0
        seen = False
        for string in s:
            if string == " " and seen:
                count += 1
                seen = False
            if string != " ":
                seen = True
                if i == len(s)-1:
                    count += 1
            i += 1

        return count