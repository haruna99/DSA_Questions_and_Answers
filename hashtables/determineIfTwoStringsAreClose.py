'''
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
'''


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        map1 = {}
        map2 = {}

        for word in word1:
            if word in map1:
                map1[word] += 1
            else:
                map1[word] = 1

        for word in word2:
            if word in map2:
                map2[word] += 1
            else:
                map2[word] = 1

        if map1.keys() != map2.keys():
            
            return False

        if sorted(list(map1.values())) != sorted(list(map2.values())):
            
            return False

        return True
    
    x = [1,2]
    # x.remove(2)
    print(x[-1::-1].index(1))