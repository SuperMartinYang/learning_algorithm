# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class List(object):
    def __init__(self, nodes):
        self.head = ListNode(0)
        cur = self.head
        for node in nodes:
            cur.next = ListNode(node)
            cur = cur.next
        self.head = self.head.next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        def reverse(tmphead, endPoint):
            pre = endPoint
            while tmphead != endPoint:
                nxt = tmphead.next
                tmphead.next = pre
                pre = tmphead
                tmphead = nxt
            return pre

        if not head:
            return None
        tailHeadList = []
        cnt = 0
        cur = head
        while cur:
            if cnt % k == 0:
                tailHeadList.append(cur)
            cur = cur.next
            cnt += 1
        if len(tailHeadList) < 2:
            return head
        for i in range(1, len(tailHeadList)):
            if i == 1:
                realhead = reverse(tailHeadList[i - 1], tailHeadList[i])
            else:
                tmpHead.next = reverse(tailHeadList[i - 1], tailHeadList[i])
            tmpHead = tailHeadList[i - 1]
        return realhead

testCase = List([1,2,3,4,5]).head
s = Solution()
s.reverseKGroup(testCase, 2)