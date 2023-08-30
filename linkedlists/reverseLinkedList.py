'''
Given the head of a singly linked list, reverse the list, and return the reversed list.


'''


class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        prev = None
        temp = head
        after = head

        while temp:
            after = after.next
            temp.next = prev
            prev = temp
            temp = after

        return prev