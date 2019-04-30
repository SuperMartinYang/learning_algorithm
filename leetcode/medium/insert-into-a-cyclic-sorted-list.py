class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def insert_into_a_cyclic_sorted_list(self, node, x):
        # if node is None
        newNode = ListNode(x)
        if not node:
            newNode.next = newNode
            return newNode

        # find the position for newNode
        flag = True
        cur = node
        while flag:
            # between two node
            if cur.val < x <= cur.next.val:
                break
            # put it to head or tail
            if cur.val > cur.next.val and (x > cur.val or x <= cur.next.val):
                break
            cur = cur.next
            if cur == node: flag = False

        newNode.next = cur.next
        cur.next = newNode
        return newNode
