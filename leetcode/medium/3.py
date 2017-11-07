# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
        Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 0 -> 8

        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        p,q = l1,l2
        carry = 0
        curr = head
        while p != None or q != None:
            x = p.val if p != None else 0
            y = q.val if q != None else 0
            sum = x + y + carry
            new_node = ListNode(sum % 10)
            carry = sum / 10
            curr.next = new_node
            curr = curr.next
            if p != None:
                p = p.next
            if q != None:
                q = q.next

        if carry > 0:
            end_node = ListNode(1)
            curr.next = end_node
        return head.next