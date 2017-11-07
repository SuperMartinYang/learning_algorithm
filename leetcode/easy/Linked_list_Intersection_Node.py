# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if self.isIntersection(headA, headB):
            return None
        # lenA = self.len_list(headA)
        # lenB = self.len_list(headB)
        # if lenA > lenB:
        #     len_dif = lenA - lenB
        # else:
        #     len_dif = lenB - lenA
        #     # A should be the one which is longer
        #     lenA, lenB, headA, headB = lenB, lenA, headB, headA
        # A_cur, B_cur = headA, headB
        # while len_dif != 0:
        #     len_dif -= 1
        #     A_cur = A_cur.next
        #
        # while A_cur != B_cur:
        #     A_cur = A_cur.next
        #     B_cur = B_cur.next
        A_cur, B_cur = headA, headB
        while A_cur != B_cur:
            A_cur = A_cur.next
            B_cur = B_cur.next
            if A_cur == None:
                A_cur = headB
            if B_cur == None:
                B_cur = headA
        return A_cur
    

    # def len_list(self, head):
    #     '''
    #     :type head: ListNode
    #     :rtype: int
    #     '''
    #     len = 0
    #     while head.next != None:
    #         len += 1
    #     return len

    def isIntersection(self, headA, headB):
        '''
        :type headA, headB: ListNode
        :rtype: bool
        '''
        if headB == None or headA == None:
            return False
        headA_end, headB_end = headA, headB
        while headA_end.next != None:
            headA_end = headA_end.next
        while headB_end.next != None:
            headB_end = headB_end.next
        if headA_end == headB_end:
            return True
        else:
            return False

