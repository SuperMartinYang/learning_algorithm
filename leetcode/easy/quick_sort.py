def quickSort(nums):
    if len(nums) <= 1: return nums
    p = partition(nums)
    left = quickSort(nums[:p])
    right = quickSort(nums[p + 1:])
    return left + [nums[p]] + right

def partition(nums):
    val = nums[0]
    buck = 0
    i, j = 0, len(nums) - 1
    while i < j:
        while i < j and nums[i] < val: i += 1
        nums[buck] = nums[i]
        buck = i
        while i < j and nums[j] > val: j -= 1
        nums[buck] = nums[j]
        buck = j
    nums[buck] = val
    return buck

print(quickSort([4,5,6,1,2,3]))