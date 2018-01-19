# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class List(object):
    def __init__(self, nums):
        self.head = ListNode(0)
        cur = self.head
        for i in nums:
            newNode = ListNode(i)
            cur.next = newNode
            cur = cur.next
        self.head = self.head.next


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        small = ListNode(0)
        big = ListNode(0)
        smallcur = small
        bigcur = big
        cur = head
        while cur:
            if cur.val < x:
                smallcur.next = cur
                smallcur = smallcur.next
            else:
                bigcur.next = cur
                bigcur = bigcur.next
            cur = cur.next
        bigcur.next = None
        smallcur.next = None
        smallcur.next = big.next
        return small.next

head = List([1,4,3,2]).head
s = Solution()
s.partition(head, 3)