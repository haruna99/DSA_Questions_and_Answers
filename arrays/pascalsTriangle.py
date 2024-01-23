'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
'''


class Solution(object):
    def generate(self, numRows):
        #################### Tine: O(n^2) Space: O(1) ####################################
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1],[1,1]]
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            n = 3
            while n <= numRows:
                temp = result[-1]
                val = []
                for i in range(len(temp)):
                    if i == 0:
                        val.append(temp[i])
                    if i == len(temp)-1:
                        val.append(temp[i])
                        break
                    val.append(temp[i]+temp[i+1])

                result.append(val)
                n += 1

        return result
        

class Solution(object):
    def generate(self, numRows):
        ############################# Dynamic Programming #################################
        ########################### Tine: O(n^2) Space: O(1) ##############################
        result = []

        for numRow in range(0, numRows):
            val = [None for _ in range(numRow+1)]
            val[0], val[-1] = 1,1

            for i in range(1, len(val)-1):
                val[i] = result[numRow-1][i-1] + result[numRow-1][i]
            result.append(val)

        return result