class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # init dict, result
        dic = {}
        result = []
        # add items to dict
        for i in nums:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        # build max_heap: heap [1...n]
        heap = []
        heap.append(None)
        heap.extend([(key, value) for key, value in dic.items()])
        self.build_max_heap(heap)
        # get result
        for i in range(k):
            a = self.get_max(heap)
            result.append(a[0])
        return result

    def build_max_heap(self, heap):
        '''
        O(n)
        heap
        '''
        len_ = len(heap)
        for i in range(len_// 2, -1, -1):
            self.max_heapify(heap, i + 1)

    def max_heapify(self, heap, index):
        '''
        O(lg n)
        '''
        r = index * 2 + 1
        l = index * 2
        len_ = len(heap)
        if r < len_ and heap[index][1] < heap[r][1]:
            largest = r
        else:
            largest = index
        if l < len_ and heap[largest][1] < heap[l][1]:
            largest = l
        if largest != index:
            self.swap(heap, index, largest)
            self.max_heapify(heap, largest)

    def get_max(self, heap):
        self.swap(heap, 1, len(heap) - 1)
        max_item = heap.pop()
        self.max_heapify(heap, 1)
        return max_item

    def swap(self, heap, i, j):
        tmp = heap[i]
        heap[i] = heap[j]
        heap[j] = tmp


s = Solution()
nums = [5,-3,9,1,7,7,9,10,2,2,10,10,3,-1,3,7,-9,-1,3,3]

print(s.topKFrequent(nums,3))