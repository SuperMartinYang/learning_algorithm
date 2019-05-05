def part(arr):
    l, r, m = 0, len(arr) - 1, len(arr) - 1
    pos, neg = 0, 0
    # pos, neg count 
    for a in arr: 
        if a < 0: neg += 1
        else: pos += 1
    req = 1
    if neg > pos: req = -1
    while l < r:
        if arr[l] * req < 0:
            # find from m
            while arr[m] * req < 0: 
                m -= 1
            arr[l], arr[m] = arr[m], arr[l]
            m = r
        req *= -1
        l += 1
    return arr

print("neg, pos: ", part([-13,-8,-12,-15,-14,35,7,-1,11,27,10,-7,-12,28,18]))