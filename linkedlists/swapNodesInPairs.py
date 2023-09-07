'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        left = head
        right = left.next
        end = dummy

        while right and left:
            left.next = right.next
            right.next = left
            end.next = right

            end = left
            
            if left:
                left = left.next
            if left:
                right = left.next
            

        return dummy.next
    
print([1,2] is [1,2])
        
