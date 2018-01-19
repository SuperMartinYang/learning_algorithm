# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# time limit exceeds
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        start = ListNode(0)
        cur = start
        while True:
            minIndex = None
            minValue = float('inf')
            for idx in range(len(lists)):
                if not lists[idx]:
                    continue
                if lists[idx].val < minValue:
                    minIndex = idx
                    minValue = lists[idx].val
            if minIndex is None:
                break
            newNode = ListNode(minValue)
            cur.next = newNode
            cur = newNode
            lists[minIndex] = lists[minIndex].next

        return start.next


# divid
class Solution(object):
    def mergeKLists(self, lists):
        def merge(left, right):
            start = ListNode(0)
            cur = start
            minval = None
            while left and right:
                if left.val < right.val:
                    minval = left.val
                    left = left.next
                else:
                    minval = right.val
                    right = right.next
                newNode = ListNode(minval)
                cur.next = newNode
                cur = newNode
            cur.next = left if left else right
            return start.next

        if not lists:
            return None
        elif len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        res = merge(left, right)
        return res