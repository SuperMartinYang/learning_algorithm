def DividAndConquer(nums):
    # split nums into several parts, reuse this function
    # the difference between dp is dp use subproblem which may different from the original problem
    return DividAndConquer(nums[:10]) + DividAndConquer(nums[10:])