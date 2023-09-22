'''
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#################### Recursion - Time:O(n) Space: O(n)  ############################
class Solution:
    def invertTree(self, root):
        if not root:
            return None

        def swap(node):
            node.left, node.right = node.right, node.left
            if node.left:
                swap(node.left)
            if node.right:
                swap(node.right)

        swap(root)
        return root

#################### BFS - Time:O(n) Space: O(n)  ############################
class Solution1:
    def invertTree(self, root):
        if root is None:
            return None

        queue = [root]

        while queue:
            new_node = queue.pop(0)
            if new_node:
                queue.append(new_node.left)
                queue.append(new_node.right)

                new_node.left, new_node.right = new_node.right, new_node.left

        return root


        