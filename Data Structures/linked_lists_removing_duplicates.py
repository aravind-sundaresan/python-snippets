# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):

        current = head

        while current != None and current.next != None:
            if current.val == current.next.val:
                current.next = current.next.next

            else:
                current = current.next

        return head
