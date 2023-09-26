'''
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
'''

###################### Time: O(n)  Space: O(n) ###########################
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        word_list = list(s)
        word_list.extend(word_list)
        word = "".join(word_list)
        if s in word[1:len(word)-1]:
            return True

        return False
    
###################### Time: O(n\sqrt(n))  Space: O(n) ###########################
class Solution1:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        n = len(s)

        for i in range(n//2):
            word = s[0:i+1]
            r = len(s)//len(word)
            if word*r == s:
                    return True

        return False