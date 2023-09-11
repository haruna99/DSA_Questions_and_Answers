'''
You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

 

Example 1:

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.
Example 2:

Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]
Explanation:
- 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
- 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
- 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
Thus, [2,0,2] is returned.
'''

################# Time: O(mlogm + nlogm)  Space: O(m) #########################
class Solution:
    def successfulPairs(self, spells, potions, success: int):
        
        result = []
        potions.sort()
        for num in spells:
            total = 0
            m = len(potions)
            left = 0
            right = m-1
            divisor = success/num
            
            while left<=right:
                mid = left + (right-left)//2
                if mid == 0:
                    if potions[mid]>= divisor:
                        total = m
                    elif potions[mid+1]>= divisor:
                        total = m-1
                    break
                else:
                    if potions[mid]>= divisor:
                        if potions[mid-1]< divisor:
                            total = m - mid
                            break
                        else:
                            right = mid
                    else:
                        left = mid + 1

            result.append(total)
        
        return result
    
################# Time: O(mlogm + nm)  Space: O(m) ###################
class Solution1:
    def successfulPairs(self, spells, potions, success: int):
        
        result = []
        potions.sort()
        for num in spells:
            total = 0
            m = len(potions)
            left = 0
            right = m-1
            divisor = success/num
            mid = left + (right-left)//2

            for i in range(m):
                if potions[i]>= divisor:
                    total = m-i
                    break
            result.append(total)

        return result


        