class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
def cycle_point_in_linklist(Linklist):
    slow = fast = Linklist
    while slow and fast and Linklist:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    fast = Linklist
    while fast != slow:
        fast = fast.next
        slow = slow.next

    return slow
