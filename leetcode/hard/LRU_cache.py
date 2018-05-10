class ListNode:
    def __init__(self, key, value):
        self.val = value
        self.key = key
        self.next = None
        self.pre = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.root = ListNode(0, 0)  # dummy node
        self.tail = ListNode(0, 0)
        self.root.next = self.tail
        self.tail.pre = self.root
        self.table = {}
        self.cnt = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.table:
            self.table[key].pre.next = self.table[key].next
            self.table[key].next.pre = self.table[key].pre
            self.table[key].pre = self.tail.pre
            self.table[key].next = self.tail
            self.tail.pre.next = self.table[key]
            self.tail.pre = self.table[key]
            return self.table[key].val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.table:
            self.table[key].pre.next = self.table[key].next
            self.table[key].next.pre = self.table[key].pre
        if self.cnt >= self.capacity:
            old_key = self.root.next.key
            del self.table[old_key]
            self.root.next.next.pre = self.root
            self.root.next = self.root.next.next

        self.table[key] = ListNode(key, value)  # put it in hash table
        self.tail.pre.next = self.table[key]
        self.table[key].pre = self.tail.pre
        self.table[key].next = self.tail
        self.tail.pre = self.table[key]
        self.cnt = self.cnt + 1 if self.cnt < self.capacity else self.capacity


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(2,1)
obj.put(2,2)
param_1 = obj.get(2)
# obj.put(key,value)
print(param_1)