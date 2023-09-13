'''Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
############################ Time: O(n)  Space: O(1) ################################
class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head

        temp = head
        while temp and temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
            

        return head

############################ Time: O(n)  Space: O(n) ################################
class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head

        prev = head
        temp = prev.next

        seen = {prev.val}
        while temp:
            if temp.val not in seen:
                prev.next = temp
                prev = temp
            seen.add(temp.val)
            temp = temp.next
        prev.next = temp

        return head