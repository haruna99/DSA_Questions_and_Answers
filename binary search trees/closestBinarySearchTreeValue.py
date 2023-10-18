'''
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.

 

Example 1:


Input: root = [4,2,5,1,3], target = 3.714286
Output: 4
Example 2:

Input: root = [1], target = 4.428571
Output: 1
 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
##################### Time: O(logn) Space: O(1) ###########################
class Solution:
    def closestValue(self, root, target: float) -> int:
        result = root.val
        min_dist = abs(root.val - target)

        temp = root

        while temp:
            value = temp.val
            new_dist = target - value
            if new_dist == 0:
                return value
            elif new_dist > 0: 
                temp = temp.right
            else:
                temp = temp.left
            if min_dist > abs(new_dist):
                min_dist = abs(new_dist)
                result = value
            elif min_dist == abs(new_dist):
                result = min(result, value)
        return result
