# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head, end = None):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # if head == end:
        #     return None
        # if head.next == end:
        #     head.next = None
        #     return head
        if not head:
            return
        last = head
        while last.next != end:
            last = last.next
        nxt = head.next
        head.next = last
        if nxt is last:
            last.next = None
        elif nxt.next is last:
            nxt.next = None
        else:
            self.reorderList(nxt, last)
            # if nxt.next is last:
            last.next = nxt


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
s = Solution()
s.reorderList(head)