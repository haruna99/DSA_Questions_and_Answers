'''
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
'''

######################### O(m+n) ############################
class Solution1:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if str1+str2 != str2+str1:
           return ""

        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]

###############  O(min(n,m)*(m+n)) ##################
from math import gcd
class Solution1:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        result = []
        seen = {}

        if len(str1)<= len(str2):
            base = str1
        else:
            base = str2

        while len(base) > 0:
            if len(str1)%len(base) != 0 or len(str2)%len(base) != 0:
               base = base[:len(base)-1]
            else:
                k1 = int(len(str1)/len(base))
                k2 = int(len(str2)/len(base))
                if base*k1==str1 and base*k2==str2:
                    return base
                else:
                    base = base[:len(base)-1]
        return base
        