# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        anchor = 0
        preHead = ListNode(0)
        current = preHead
        while not (l1 == None and l2 == None and anchor == 0):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + anchor
            anchor = sum // 10
            node = ListNode(sum % 10)
            current.next = node
            current = node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return preHead.next
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        