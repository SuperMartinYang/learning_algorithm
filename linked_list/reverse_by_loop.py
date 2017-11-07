class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


def reverse_by_loop(Linklist):
    '''

    :param Linklist: ListNode
    :return: ListNode
    '''
    next_ = pre_ = ListNode(0)
    if Linklist == None or Linklist.next == None:
        return Linklist
    while Linklist != None:
        next_ = Linklist.next
        Linklist.next = pre_
        pre_ = Linklist
        Linklist = next_
    return pre_



