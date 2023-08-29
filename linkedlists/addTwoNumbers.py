'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        remainder = 0
        
        result = ListNode()
        temp = result

        temp1 = l1
        temp2 = l2
        while temp1 and temp2:
            new_sum = temp1.val + temp2.val + remainder
            if new_sum >= 10:
                new_sum -= 10
                remainder = 1
            else:
                remainder = 0
            temp1 = temp1.next
            temp2 = temp2.next
            
            temp.next = ListNode(new_sum)
            temp = temp.next

        while temp1:
            new_sum = temp1.val + remainder
            if new_sum >= 10:
                new_sum -= 10
                remainder = 1
            else:
                remainder = 0
            temp1 = temp1.next
            
            temp.next = ListNode(new_sum)
            temp = temp.next
        
        while temp2:
            new_sum = temp2.val + remainder
            if new_sum >= 10:
                new_sum -= 10
                remainder = 1
            else:
                remainder = 0
            temp2 = temp2.next

            temp.next = ListNode(new_sum)
            temp = temp.next
            
        if remainder == 1:
            temp.next = ListNode(remainder)
           

        return result.next