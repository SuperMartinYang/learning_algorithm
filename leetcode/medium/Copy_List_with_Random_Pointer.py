# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dic = collections.defaultdict(RandomListNode)
        cur = head
        while cur:
            newNode = RandomListNode(cur.label)
            dic[cur] = newNode
            cur = cur.next
        dummy = RandomListNode(0)
        cur = dummy
        curH = head
        while curH:
            cur.next = dic[curH]
            cur.next.random = dic[curH.random]
            cur = cur.next
            curH = curH.next
        return dummy.next

head = cur = RandomListNode(-1)
Solution().copyRandomList()
