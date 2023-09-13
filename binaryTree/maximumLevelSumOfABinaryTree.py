'''
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root) -> int:
        if not root:
            return 0
        
        queue = [root]
        level = 0
        maximum = [1, root.val]
        while queue:
            n = len(queue)
            current_sum = 0
            level += 1 
            for _ in range(n):
                node = queue.pop(0)
                current_sum += node.val
                if node.left:
                    queue.append( node.left)
                if node.right:
                    queue.append(node.right)
            
            if current_sum > maximum[1]:

                maximum[0] = level
                maximum[1] = current_sum
            
        return maximum[0]
    

class Solution1:
    def maxLevelSum(self, root) -> int:
        if not root:
            return 0
        
        queue = [(1, root)]

        result = []

        while queue:
            level, node = queue.pop(0)
            if node.left:
                queue.append((level+1, node.left))
            if node.right:
                queue.append((level+1, node.right))

            result.append((level, node.val))
        
        my_dict = {}
        for val in result:
            if val[0] in my_dict:
                my_dict[val[0]] += val[1]
            else:
                my_dict[val[0]] = val[1]

        maximum = [1, my_dict[1]]

        for val in my_dict:
            if my_dict[val] > maximum[1]:
                maximum[0] = val
                maximum[1] = my_dict[val]

        
        return int(maximum[0])