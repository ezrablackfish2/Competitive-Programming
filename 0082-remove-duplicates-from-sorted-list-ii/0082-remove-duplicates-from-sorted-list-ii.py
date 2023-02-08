# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        
        if not head or not head.next:
            return head

        pre = dummy = ListNode(0,head)
        while head and head.next:
            while head.next and head.val == head.next.val:
                head = head.next
            if pre.next == head:
                pre = pre.next
                
            else:
                pre.next = head.next
                
            head = head.next

        return dummy.next
        """
        :type head: ListNode
        :rtype: ListNode
        """
        