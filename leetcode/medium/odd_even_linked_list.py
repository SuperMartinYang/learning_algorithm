# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = ListNode(1)
        o_cur = odd
        even = ListNode(2)
        e_cur = even
        cur = head
        cnt = 1
        while cur and cnt <= 5:
            if cnt % 2 == 1:
                o_cur.next = cur
                o_cur = o_cur.next
                o_cur.next = None
            else:
                e_cur.next = cur
                e_cur = e_cur.next
                e_cur.next = None
            cur = cur.next
            cnt += 1
        o_cur.next = even.next
        return odd.next

head = cur = ListNode(1)
new = ListNode(2)
cur.next = new
cur = new
new = ListNode(3)
cur.next = new

print(Solution().oddEvenList(head))