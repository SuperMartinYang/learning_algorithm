def BinarySearch(nums, tgt):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (hi + lo) // 2
        # for some specific condition, update lo and hi
        if nums[mid] > tgt: hi = mid - 1
        else: lo = mid + 1

    return lo   # the index of first larger, lo - 1 means the last smaller, lo range [0, len(nums)]