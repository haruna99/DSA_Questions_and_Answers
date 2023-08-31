'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for string in s:
            if string in "({[":
                stack.append(string)
                continue
            if len(stack)==0:
                return False
            if string == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            if string == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False

            if string == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        if len(stack)>0:
            return False

        return True