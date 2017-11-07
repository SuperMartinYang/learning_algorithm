class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None



def deleteNode(LinkList,node):
    '''

    :param LinkList: ListNode
    :param node: ListNode
    :return:
    '''
    if LinkList == None or LinkList.next == None:
        return None
    next_node = node.next
    node.val = next_node.val
    node.next = next_node.next
    del next_node


LinkList = ListNode(10)
LinkList.next = ListNode(9)
