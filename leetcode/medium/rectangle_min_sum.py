def minSum(nums):
    """
    smallest sum
    :param nums: list[list]
    :return: int
    """
    rows = len(nums)
    cols = len(nums[0]) if rows else 0
    for r in range(1, rows):
        for c in range(cols):
            tmp = nums[r][c] + 1e9
            for k in (-1, 0, 1):
                if k + c < 0 or k + c >= cols:
                    continue
                tmp = min(tmp, nums[r][c] + nums[r - 1][c + k])
            nums[r][c] = tmp
    res = 1e9
    for n in nums[-1]:
        res = min(res, n)
    return res

print(minSum([[1,2,3,4,5],[9,8,7,6,5]]))