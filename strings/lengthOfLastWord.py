'''

'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        seen = False

        for i in range(-1, -len(s)-1, -1):
            if s[i] != " ":
                seen = True
                result += 1
            else:
                if seen:
                    break
        
        return result