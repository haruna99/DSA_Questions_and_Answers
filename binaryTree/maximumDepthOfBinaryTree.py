'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


############### BFS ######################
################# Time: O(n)  Space: O(log n)
class Solution:
    def maxDepth(self, root) -> int: 
        if root is None:
            return 0

        max_depth = 0
        stack = [(1,root)]
        while stack:
            curr_depth, root = stack.pop(0)
            if root is not None:
                max_depth = max(curr_depth, max_depth)
                stack.append((curr_depth + 1, root.left))
                stack.append((curr_depth + 1, root.right))

        return max_depth


############## DFS ######################
################# Time: O(n)  Space: O(log n)
class Solution1:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        return 1 + max(left_height, right_height)


        
        

        

        

