# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or not head or not head.next:
            return head
        # length of list
        cur = head
        cnt = 1
        while cur.next:
            cur = cur.next
            cnt += 1
        real_k = k % cnt
        # rotate
        prehead = ListNode(0)
        prehead.next = head
        tail = prehead
        while real_k > 0:
            tail = tail.next
            real_k -= 1
        while tail.next:
            prehead = prehead.next
            tail = tail.next
        res = prehead.next
        prehead.next = None
        tail.next = head
        return res

List = ListNode(1)
List.next = ListNode(2)
s = Solution()
s.rotateRight(List, 2)