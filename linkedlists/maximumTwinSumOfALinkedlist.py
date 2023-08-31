'''
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

###################### Time O(n)  Space: O(1) #########################
class Solution:
    def pairSum(self, head) -> int:
        slow = head
        fast = head

        while fast:
            slow = slow.next
            fast = fast.next.next

        prev = None
        after = slow

        while slow:
            after = after.next
            slow.next = prev 
            prev = slow
            slow = after
        
        first = head
        maximum = float("-inf")
        while prev:
            maximum = max(maximum,first.val + prev.val)
            first = first.next
            prev = prev.next

        return maximum
    

######################## Time: O(n)  Space: O(n) ########################
class Solution:
    def pairSum(self, head) -> int:
        values = []
        temp = head
        while temp:
            values.append(temp.val)
            temp = temp.next

        i=0
        j = len(values)-1
        max_sum = float("-inf")
        while i<j:
            new_sum = values[i]+values[j]
            max_sum = max(max_sum, new_sum)
            i+= 1
            j-= 1

        return max_sum