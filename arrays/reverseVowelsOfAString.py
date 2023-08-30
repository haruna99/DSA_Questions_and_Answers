'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) <= 1:
            return s
        vowels = {"a","e","i","o","u","A", "E", "I", "O", "U"}
        lst = list(s)
        i = 0
        j = len(s)-1
        
        while i < j:
            if lst[i] not in vowels:
                i += 1
                
            if s[j] not in vowels:
                j -= 1

            if lst[i] in vowels and lst[j] in vowels:
                lst[i], lst[j] = lst[j], lst[i]            

                i+=1
                j-=1
            
        return "".join(lst)