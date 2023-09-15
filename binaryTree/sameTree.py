'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        
        stack1 = [p]  #### Implement with linkedlist
        result1 = []

        while stack1:
            node = stack1.pop()
            if node:
                result1.append(node.val)
                stack1.append(node.left)
                stack1.append(node.right)
            else:
                result1.append(node)

        stack2 = [q]  #### Implement with linkedlist
        result2 = []

        while stack2:
            node = stack2.pop()
            if node:
                result2.append(node.val)
                stack2.append(node.left)
                stack2.append(node.right)
            else:
                result2.append(node)

        return result1 == result2
