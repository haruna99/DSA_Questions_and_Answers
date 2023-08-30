'''
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head):
        temp = head
        odd = ListNode(0)
        odd_head = odd
        even = ListNode(-1)
        even_head = even

        i=1
        while temp:
            if i % 2 == 0:
                even.next = temp
                even = even.next
            else:
                odd.next = temp
                odd = odd.next
            temp = temp.next
            i+= 1
        
        odd.next = None
        even.next = None 

        odd.next = even_head.next
        
        head = odd_head.next
        odd_head.next = None

        return head