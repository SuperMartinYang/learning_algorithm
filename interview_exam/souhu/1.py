#coding=utf-8
import sys
def solver(n, k, values):
    res = []
    def findKthSmallest(values, p):
        # find p in O(log n)
        def swap(i, j):
            tmp = values[i]
            values[i] = values[j]
            values[j] = tmp

        def quickselect(start, end):
            pivot = values[end]
            small, big = start, start
            while small < end:
                if values[small] <= pivot:
                    swap(big, small)
                    big += 1
                small += 1
            swap(big, end)
            if big == p:
                return pivot
            elif big < p:
                return quickselect(big + 1, end)
            else:
                return quickselect(start, big - 1)

        return quickselect(0, len(values) - 1)
    for i in range(k):
        res.append(findKthSmallest(values, i))
    return res

if __name__ == "__main__":
    # 读取第一行的n, k
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    n, k = map(int, line.split())
    ans = 0
    # element
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = map(int, line.split())
    ans = solver(n, k, [v for v in values])
    print(','.join([str(i) for i in ans]))