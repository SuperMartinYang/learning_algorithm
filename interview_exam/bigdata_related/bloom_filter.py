####################################################
#              v1 -       -- v2 -
#             / \   \   / /       \
#            |   |   | | |         |
#  0 0 0 0 0 1 0 1 0 1 1 1 0 0 0 0 1 0 0 0
####################################################

class bitarray(list):
    def __init__(self, nums):
        list.__init__([0 for _ in range(nums)])

class Hashes():
    def hash(self, idx):
        return 

MAXNUM = 1000
class bloom_filter:
    def __init__(self):
        self.barr = bitarray(MAXNUM)

    def add(self, url):
        hashes = self.gethash(url)
        for h in hashes:
            self.barr[h] = 1

    def contains(self, url):
        hashes = self.gethash(url)
        for h in hashes:
            if self.barr[h] != 0:
                return False
        return True


    def gethash(self, url):
        h0 = Hashes.hash(url, 0)
        h1 = Hashes.hash(url, 1)
        h2 = Hashes.hash(url, 2)
        h3 = Hashes.hash(url, 3)
        h4 = Hashes.hash(url, 4)
        h5 = Hashes.hash(url, 5)
        h6 = Hashes.hash(url, 6)
        h7 = Hashes.hash(url, 7)
        return [h0, h1, h2, h3, h4, h5, h6, h7]

