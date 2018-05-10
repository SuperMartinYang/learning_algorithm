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
# def quicksort(lst, lo, hi):
#     if lo < hi:
#         p = partition(lst, lo, hi)
#         quicksort(lst, lo, p)
#         quicksort(lst, p+1, hi)
#     return
#
# def partition(lst, lo, hi):
#     pivot = lst[hi-1]
#     i = lo - 1
#     for j in range(lo, hi):
#         if lst[j] < pivot:
#             i += 1
#             lst[i], lst[j] = lst[j], lst[i]
#     if lst[hi-1] < lst[i+1]:
#         lst[i+1], lst[hi-1] = lst[hi-1], lst[i+1]
#     return i+1
quicksort([3,2,1,8,5,0], 0, 6)
