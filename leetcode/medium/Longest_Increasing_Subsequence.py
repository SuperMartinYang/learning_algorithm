def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums == []:
        return 0
    len_nums = len(nums)
    dp = [-1] * len_nums
    dp[0] = 1
    maxall = 1

    for i in range(1, len_nums):
        inter = 0
        for j in range(i):
            if nums[j] < nums[i]:
                inter = max(inter, dp[j])
        dp[i] = inter + 1
        maxall = max(maxall, dp[i])

    return maxall

print(lengthOfLIS([10,9,2,5,3,7,101,18]))