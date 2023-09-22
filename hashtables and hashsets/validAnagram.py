'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        my_dict = {}


        for i in range(len(s)):
            if s[i] in my_dict:
                my_dict[s[i]] += 1
            else:
                my_dict[s[i]] = 1

        for j in range(len(t)):
            if t[j] not in my_dict:
                return False
            my_dict[t[j]] -= 1

        
        for letter in my_dict:
            if my_dict[letter] != 0:
                return False
        return True