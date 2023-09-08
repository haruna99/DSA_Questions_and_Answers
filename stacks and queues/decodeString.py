'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
'''

class Solution:
    def decodeString(self, s: str) -> str:
        alphabets = {
            "a", "b", "c", "d", "e", "f", "g","h",
            "i", "j","k","l","m","n","o","p","q","r","s","t",
            "u","v","w","x","y","z"
            }
        numbers = {
            "0","1","2","3","4","5","6","7","8","9"
            }
        stack = []

        for string in s:
            if string != "]":
                stack.append(string)
                print(stack)
            else:
                current = ""
                while stack[-1] != "[":
                    current += stack.pop()
                stack.pop()
                val = []
                while stack and stack[-1] in numbers:
                    val.append(stack.pop())
                    value = int("".join(val[::-1]))
                current = current[::-1]
                current *= value
                for curr in current:
                    stack.append(curr)

        return "".join(stack)


                    

        