'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        my_map = {}
        seen = {}

        i = 0
        count = 0
        words = s.split(' ')

        for word in words:
            if count >= len(pattern):
                return False
            letter = pattern[count]

            if word not in seen:
                seen[word] = letter
                
            if (letter in my_map and word != my_map[letter]) or seen[word] != letter:
                return False
            else:
                my_map[letter] = word
            count += 1

        return count == len(pattern)