class ListNode:
    '''
    self.next: ListNode
    '''
    def __init__(self):
        self.val = None
        self.next = None

class LinkList:
    def __init__(self):
        self.cur_node = None

    def add_node(self,x):
        node = ListNode()
        node.val = x
        node.next = self.cur_node   # so that the end is also ListNode
        self.cur_node = node

    def print_link_list(self):
        node = self.cur_node
        while node != None:
            print(node.val)
            node = node.next

    def form_list(self,ran):
        for i in range(ran):
            self.add_node(i)

    def get_last_k(self,k):
        now = pre = self.cur_node
        for i in range(k):
            pre = pre.next
        while pre != None:
            now = now.next
            pre = pre.next
        return now

    def get_mid(self):
        '''
        get mid item
        :return:
        '''
        slow = fast = self.cur_node
        while fast and slow and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

def reverse_by_recursive(node):
    # first condition is to check error, the second is to return
    if node == None or node.next == None:
        return node

    newList = reverse_by_recursive(node.next)

    newList.next.next = newList
    newList.next = None
    return newList

ll = LinkList()

ll.form_list(10)
ll.print_link_list()

ll2 = reverse_by_recursive(ll.cur_node)