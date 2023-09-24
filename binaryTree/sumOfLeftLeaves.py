'''
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


############################# DFS (Recursion) - Time: O(n)  Space: O(n) #################################
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        
        if root is None:
            return 0
        result = []
        def traverse(node):
            
            if node.left:
                if node.left.left is None and node.left.right is None:
                    result.append(node.left.val)
                else:
                    traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(root)
        print(result)
        return sum(result)
        

############################# DFS (Iteration) - Time: O(n)  Space: O(n) ######################################
class Solution1:
    def sumOfLeftLeaves(self, root) -> int:
        if not root:
            return 0

        stack = [[None, root]]
        total = 0

        while stack:
            position, node = stack.pop()
            if not node.left and not node.right and position == 'left':
                total += node.val

            if node.left:
                stack.append(['left', node.left])
            if node.right:
                stack.append(['right', node.right])

        return total


