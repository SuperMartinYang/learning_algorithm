def quicksort(arr, start, stop):
    if start < stop:
        pivot = start
        pos = partition(pivot, arr, start, stop)
        quicksort(arr, start, pos)
        quicksort(arr, pos + 1, stop)

def partition(pivot, arr, start, stop):
    p = arr[pivot]
    i = start - 1
    for j in range(start, stop):
        if arr[j] < p:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    if arr[i + 1] >= arr[stop - 1]:
        arr[stop - 1], arr[i + 1] = arr[i + 1], arr[stop - 1]
    return i + 1
#
def quicksort_c(lst, lo, hi):
    if lo < hi:
        p = partition_c(lst, lo, hi)
        quicksort_c(lst, lo, p - 1)
        quicksort_c(lst, p+1, hi)
    return lst

def partition_c(lst, lo, hi):
    pivot = lst[hi]
    while lo < hi:
        while lo < hi and lst[lo] < pivot:
            lo += 1
        lst[hi] = lst[lo]
        hi -= 1
        while lo < hi and lst[hi] > pivot:
            hi -= 1
        lst[lo] = lst[hi]
        lo += 1
    lst[hi] = pivot
    return hi
print(quicksort_c([3,2,1,8,5,0], 0, 5))
