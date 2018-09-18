# Program to reverse a singly linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        current = head
        previous = None
        next_node = None

        while current != None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        head = previous

        return head
