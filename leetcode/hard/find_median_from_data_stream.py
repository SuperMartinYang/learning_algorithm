import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # min heap for right part, max heap for left part
        self.minHeap_right = []
        self.maxHeap_left = []
        self.tot_num = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.maxHeap_left:
            heapq.heappush(self.maxHeap_left, -num)
        elif not self.minHeap_right:
            if self.maxHeap_left[0] > num:
                heapq.heappush(self.minHeap_right, -heapq.heappop(self.maxHeap_left))
                heapq.heappush(self.maxHeap_left, -num)
            else:
                heapq.heappush(self.minHeap_right, num)
        elif num > self.minHeap_right[0]:
            if len(self.maxHeap_left) > len(self.minHeap_right):
                heapq.heappush(self.minHeap_right, num)
            else:
                heapq.heappush(self.maxHeap_left, -heapq.heappop(self.minHeap_right))
                heapq.heappush(self.minHeap_right, num)
        elif num <= self.maxHeap_left[0]:
            if len(self.maxHeap_left) > len(self.minHeap_right):
                heapq.heappush(self.minHeap_right, -heapq.heappop(self.maxHeap_left))
                heapq.heappush(self.maxHeap_left, -num)
            else:
                heapq.heappush(self.maxHeap_left, -num)
        elif self.maxHeap_left < num < self.minHeap_right[0]:
            if len(self.maxHeap_left) > len(self.minHeap_right):
                heapq.heappush(self.minHeap_right, num)
            else:
                heapq.heappush(self.maxHeap_left, -num)

        self.tot_num += 1

    def findMedian(self):
        """
        :rtype: float
        """
        return float(-self.maxHeap_left[0] + self.minHeap_right[0]) / 2 if self.tot_num % 2 == 0 else -float(self.maxHeap_left[0])


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
param_2 = obj.findMedian()
obj.addNum(3)
param_3 = obj.findMedian()
print(param_2, param_3)