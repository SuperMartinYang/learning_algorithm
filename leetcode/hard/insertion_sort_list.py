# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        pre_table = {}
        dum = ListNode(float('-inf'))
        dum.next = head
        cur = dum
        while cur.next:
            pre_table[cur.next] = cur
            cur = cur.next
        cur = head.next
        while cur:
            target = pre_table[cur]
            while target.val > cur.val:
                target = pre_table[target]
            tmp = target.next
            target.next = cur
            tmp_n = cur.next
            cur.next = tmp
            pre_table[cur].next = tmp_n
            pre_table[tmp_n] = pre_table[cur]
            cur = tmp_n
        return dum.next


head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
Solution().insertionSortList(head)