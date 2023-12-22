'''
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

 

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
'''

class Solution(object):
    def findWords(self, words):
        my_dict = {'q':1,'w':1,'e':1,'r':1,'t':1,'y':1,'u':1,'i':1,'o':1,'p':1,'a':2,'s':2,
        'd':2,'f':2,'g':2,'h':2,'j':2,'k':2,'l':2,'z':3,'x':3,'c':3,'v':3,'b':3,'n':3,'m':3}

        result = []
        for word in words:
            init = word[0].lower()
            step = my_dict[init]
            count = 0
            for letter in word:
                letter = letter.lower()
                curr = my_dict[letter] 
                if curr != step:
                    break
                count += 1

            if count == len(word):
                result.append(word)
                
        return result

        