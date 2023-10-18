'''
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
 
'''

class Solution:
    def equalPairs(self, grid) -> int:
        ################### TIme: O(n^2)  Space: O(n^2) ########################
        result = 0
        n = len(grid)
        rows = {}
        columns = []
        for row in range(n):
            new_row = tuple(grid[row])
            if new_row in rows:
                rows[new_row] +=1
            else:
                rows[new_row] = 1
            new_val = []
            for col in range(n):
                new_val.append(grid[col][row])
            columns.append(tuple(new_val))

        for col in columns:
            if col in rows:
                result += rows[col]

        return result
    