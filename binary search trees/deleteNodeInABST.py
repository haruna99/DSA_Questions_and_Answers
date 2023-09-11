'''
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

################## Time: O(log n)   Space: O(log n) #######################
class Solution:
    def minimum(self, node):
        while node.left:
            node = node.left
        return node.val

    def __delete(self,node, key):
        if node is None:
            return None
        if key < node.val:
            node.left = self.__delete(node.left, key)
        elif key > node.val:
            node.right = self.__delete(node.right, key)
        else:  
            if node.left is None and node.right is None:
                node = None
            elif node.right is None:
                node = node.left
            elif node.left is None:
                node = node.right
            else:
                min_val = self.minimum(node.right)
                node.val = min_val
                node.right = self.__delete(node.right, min_val)

        return node


    def deleteNode(self, root, key: int):
        return self.__delete(root, key)
