''
'''
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"
 

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 104
'''

class Solution(object):
    ################################ Time: O(n)  Space: O(n) ###############################
    def reverseStr(self, s, k):
        result = []
        n = len(s)
        i = 0
        while i < n:
            if i+2*k < n:
                string = s[i:i+2*k]
            else:
                string = s[i:]
            if k > len(string):
                result.append(string[::-1])
            else:
                result.append(string[:k][::-1])
                result.append(string[k:])

            i += 2*k

        return "".join(result)

        