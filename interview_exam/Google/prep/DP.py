def TopDownDP():

    return

def BottomUpDP():
    # use memo to memoize the bottom result, for up to use
    dp = []
    for i in range(len(nums)):
        dp[i + 1] = dp[i] # when some condition
    return dp[10]
