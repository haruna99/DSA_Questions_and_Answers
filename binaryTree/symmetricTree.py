'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: fals
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

###################### Iterative ##########################
class Solution:
    def isSymmetric(self, root) -> bool:
        if  root is None:
            return True

        left = root.left 
        right = root.right

        stack1 = [left]
        stack2 = [right]
        result1 = []
        result2 = []

        while stack1 and stack2:
            node1 = stack1.pop(0)
            node2 = stack2.pop(0)
            if node1:
                result1.append(node1.val)
                stack1.append(node1.left)
                
                stack1.append(node1.right)
            else:
                result1.append(node1)

            if node2:
                result2.append(node2.val)

                stack2.append(node2.right)
                stack2.append(node2.left)
            else:
                result2.append(node2)
            
        return result1 == result2


###################### Recursive ##########################
class Solution1:
    def isSymmetric(self, root) -> bool:

        def checker(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False


            return (node1.val == node2.val) and checker(node1.left, node2.right) and checker(node1.right, node2.left)

        return checker(root.left, root.right)

        