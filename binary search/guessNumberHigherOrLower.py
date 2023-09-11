'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

 

Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1
'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

############ Binary search --- Time: O(Log2n) Space: O(1) ###############
class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        
        while True:
            mid = left + (right-left)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                left = mid+1
            else:
                right = mid-1

        

############ Ternary search --- Time O(Log3n) Space: O(1) #################
class Solution1:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while True:
            mid1 = left + (right-left)//3
            mid2 = right - (right-left)//3
            if guess(mid1) == 0:
                return mid1
            elif guess(mid2) == 0:
                return mid2
            elif guess(mid1) == 1 and guess(mid2) == -1:
                left = mid1+1
                right = mid2-1
            elif guess(mid1) == -1:
                right = mid1-1
            
            elif guess(mid2) == 1:
                left = mid2