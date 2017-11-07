# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        curr = newListNode = ListNode(0)
        p, q = l1, l2

        while q and p:
            if p.val < q.val:
                curr.next = p
                p = p.next
            else:
                curr.next = q
                q = q.next
            curr = curr.next
        curr.next = q or p
        return newListNode.next

s = Solution()
s.mergeTwoLists(l1 = ListNode(3) , l2 = ListNode(5))