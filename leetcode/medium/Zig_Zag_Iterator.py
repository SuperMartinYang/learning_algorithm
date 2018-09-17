class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    def __init__(self, v1, v2):
        # do intialization if necessary
        self.whole = []
        m = len(v1)
        n = len(v2)
        cnt, i, j = 0, 0, 0
        while cnt < m + n:
            if cnt & 1 == 0:
                self.whole.append(v1.pop(0) if v1 else v2.pop(0))
            else:
                self.whole.append(v2.pop(0) if v2 else v1.pop(0))
            cnt += 1
        print(self.whole)
    """
    @return: An integer
    """
    def next(self):
        # write your code here
        return self.whole.pop(0)
    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        return self.whole != []

it = ZigzagIterator([1,3,5], [4,6,9,10])
while it.hasNext(): print(it.next())