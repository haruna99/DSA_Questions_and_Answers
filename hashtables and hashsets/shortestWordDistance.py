'''
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

 

Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Outp
'''

class Solution:
    def shortestDistance(self, wordsDict, word1: str, word2: str) -> int:
        seen = {
            word1: -1,
            word2: -1
        }

        count = 0
        result = len(wordsDict)-1

        for word in wordsDict:
            if word in seen:
                seen[word] = count
            x = seen[word1]
            y = seen[word2]
            if x >= 0 and y >= 0:
                result = min(result, abs(x-y))

            count += 1

        return result