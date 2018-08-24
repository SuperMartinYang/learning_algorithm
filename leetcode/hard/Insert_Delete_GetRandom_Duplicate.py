import collections
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.locations = collections.defaultdict(list)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        flag = False
        if val not in self.locations:
            flag = True
        self.nums.append(val)
        self.locations[val].append(len(self.nums) - 1)
        return flag

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.locations:
            idx = self.locations[val].pop()
            if idx != len(self.nums) - 1:
                self.nums[idx] = self.nums[-1]
                self.locations[self.nums[-1]].remove(len(self.nums) - 1)
                self.locations[self.nums[-1]].append(idx)
            self.nums.pop()
            if not self.locations[val]: del self.locations[val]
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        r = random.randint(0, len(self.nums) - 1) if len(self.nums) > 1 else 0
        return self.nums[r]


s = RandomizedCollection()
s.insert(10)
s.insert(10)
s.insert(20)
s.insert(20)
s.insert(30)
s.insert(30)
s.remove(10)
s.remove(10)
s.remove(30)
s.remove(30)
