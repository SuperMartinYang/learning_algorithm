def find_min_in_rotate_array(arr):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (hi + lo) // 2
        if arr[mid] < arr[(mid - 1) % len(arr)] and arr[mid] < arr[(mid + 1) % len(arr)]: return arr[mid]
        elif (arr[mid] < arr[hi]): hi = mid - 1
        else: lo = mid + 1
    
    return arr[lo]

print(find_min_in_rotate_array([3,4,5,6,7,1]))