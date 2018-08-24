# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        reverse list
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = self.reverse_list(l1)
        l2 = self.reverse_list(l2)
        carry = 0
        cur_1 = l1
        cur_2 = l2
        res = ListNode(0)
        cur = res
        while cur_1 or cur_2:
            if cur_1 and cur_2:
                cur.next = ListNode((cur_1.val + cur_2.val + carry) % 10)
                carry = (cur_1.val + cur_2.val + carry) // 10
                cur_1 = cur_1.next
                cur_2 = cur_2.next
            else:
                tmp = cur_1 or cur_2
                cur.next = ListNode((tmp.val + carry) % 10)
                carry = (tmp.val + carry) // 10
                cur_1 = cur_1.next if cur_1 else None
                cur_2 = cur_2.next if cur_2 else None
            cur = cur.next
        if carry:
            cur.next = ListNode(carry)
        return self.reverse_list(res.next)

    def reverse_list(self, head):
        pre = None
        while head:
            _next = head.next
            head.next = pre
            pre = head
            head = _next
        return pre

    def addTwoNumbers2(self, l1, l2):
        """
        use stack
        :param l1:
        :param l2:
        :return:
        """