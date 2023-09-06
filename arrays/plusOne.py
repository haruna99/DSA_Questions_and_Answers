'''
Prove that lim
n!1
n1=n = 1.

'''

################### Time: O(n)   Space: O(1) #####################
class Solution:
    def plusOne(self, digits):
        carry = 0
        n = len(digits)
        for i in range(-1,-n-1,-1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                carry = 1
        if carry == 1:
            digits.append(1)
        i = 0
        n = len(digits)
        for j in range(n-1):
            digits[i], digits[n-1] = digits[n-1], digits[i]
            i+= 1

        return digits


############### Time: O(n)  Space: O(n) #########################
class Solution1:
    def plusOne(self, digits):
        number = 0
        n = len(digits)
        for i in range(n):
            number += digits[i]*10**(n-i-1)
        number += 1
        string = str(number)
        result = []
        for num in string:
            result.append(int(num))

        return result