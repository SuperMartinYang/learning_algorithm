# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True
        ll = self.len_list(head)
        p1 = p2 = head
        half_way = ll / 2
        while half_way >= 1:
            p2 = p2.next
            half_way -= 1
        # reverse pre-half
        next_ = pre_ = None
        while head != p2:
            next_ = head.next
            head.next = pre_
            pre_ = head
            head = next_
        if ll % 2 == 1:
            p2 = p2.next
        while p2 and pre_:
            if pre_.val != p2.val:
                return False
            p2 = p2.next
            pre_ = pre_.next
        return True

    def len_list(self, head):
        l = 0
        cur = head
        while cur != None:
            l += 1
            cur = cur.next
        return l