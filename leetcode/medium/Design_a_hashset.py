class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.initLen = 1000000
        self.dic = [-1] * self.initLen
        self.used = 0

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        i = hash(key) % self.initLen
        if self.dic[i] == -1:
            # not used
            self.dic[i] = key

        else:
            # double hash, find empty
            while self.dic[i] != key and self.dic[i] != -1:
                # double hash
                i = hash(i) % self.initLen
            self.dic[i] = key

        self.used += 1
        # remap
        if self.used >= self.initLen / 2:
            self.initLen *= 2
            d = [0] * (self.initLen)
            for i in range(len(self.dic)):
                if self.dic[i] != -1:
                    d[hash(self.dic[i])] = self.dic[i]
            self.dic = d

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        i = hash(key) % self.initLen
        while self.dic[i] != key and self.dic[i] != -1:
            i = hash(i) % self.initLen
        if self.dic[i] == key:
            self.dic[i] = -1
            self.used -= 1

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        i = hash(key) % self.initLen
        while self.dic[i] != key and self.dic[i] != -1:
            i = hash(i) % self.initLen
        if self.dic[i] == -1: return False
        return True

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)