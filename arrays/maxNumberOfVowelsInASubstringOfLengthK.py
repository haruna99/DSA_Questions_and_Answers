'''
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a","e","i","o","u"}

        new_count = 0
        for string in s[:k]:
            if string in vowels:
                new_count += 1

        maximum = new_count

        i = 1
        j = k

        while j < len(s):
            if s[i-1] in vowels:
                new_count -= 1
            if s[j] in vowels:
                new_count += 1
            maximum = max(new_count, maximum)

            i += 1
            j += 1
        
        return maximum