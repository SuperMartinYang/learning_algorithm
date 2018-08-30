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



class Solution(object):
    def lengthOfLISubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # stack doesn't work. it works in longest increasing subarray, time: O(N)
        stack = []
        longest = 0
        for num in nums:
            if not stack or num > stack[-1]:
                stack.append(num)
            else:
                longest = max(longest, len(stack))
                while stack and num <= stack[-1]:
                    stack.pop()
                stack.append(num)
        return max(longest, len(stack))

    def lengthOfLIS(self, nums):
        tails = [0] * len(
            nums)  # tail is an array which stores the smallest tail of all increasing subsequence with length i + 1 in tails[i]
        size = 0
        for num in nums:
            # since tail[0 .. size] is increasing, use binary search to update tail
            # when tail[i - 1] < num < tail[i]
            i, j = 0, size
            while i != j:
                mid = (j - i) / 2 + i
                if tails[mid] < num:
                    i = mid + 1
                else:
                    j = mid
            tails[i] = num
            size = max(i + 1, size)
        return size

print(lengthOfLIS([10,9,2,5,3,7,101,18]))