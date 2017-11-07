class Solution(object):
    def binary_search(self,list, key):
        min, max = 0, len(list)
        while min <= max:
            i = int((min + max) / 2)
            if list[i] > key:
                max = i - 1
            elif list[i] < key:
                min = i + 1
            else:
                return i



list = [1,2,3,4,5,6,7,8,9,10]   # should be orderred
s = Solution()
print(s.binary_search(list,10))
