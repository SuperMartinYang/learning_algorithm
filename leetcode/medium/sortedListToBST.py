# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        slow = head
        fast = head
        if not head or not head.next:
            return head
        pre = head
        while slow and fast and fast.next:
            if slow != head:
                pre = pre.next
            slow = slow.next
            fast = fast.next.next
        mid = slow
        root = TreeNode(mid.val)
        pre.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

s = Solution()
s.sortedListToBST(head)