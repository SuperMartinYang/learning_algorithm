def mergeSort(nums):
    if len(nums) <= 1: return nums
    mid = len(nums) // 2
    left = mergeSort(nums[0:mid])
    right = mergeSort(nums[mid:])
    newNums = merge(left, right)
    return newNums

def merge(left, right):
    res = [0] * (len(left) + len(right))
    i, j, cur = 0, 0, 0
    while i < len(left) or j < len(right):
        litem = left[i] if i < len(left) else 1e9
        ritem = right[j] if j < len(right) else 1e9
        if litem < ritem: 
            res[cur] = litem
            i += 1
        else: 
            res[cur] = ritem
            j += 1
        cur += 1
    return res

print(mergeSort([4,5,2,1,7,9]))