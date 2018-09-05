import copy
class Solution(object):
    def paint_house_ii(self, costs):
        # also has an approach with don't use any extra space, record, min1, min2 and minVal1, minVal2
        if not costs: return 0
        dp = copy.deepcopy(costs)
        # record the idx of min, and second min spend on i - 1 house
        min1, min2 = -1, -1
        for i in range(1, len(costs)):
            pre1, pre2 = min1, min2
            min1, min2 = -1, -1
            for j in range(k):
                if j != pre1:
                    dp[i][j] += 0 if pre1 == -1 else dp[i - 1][pre1]
                else:
                    dp[i][j] += 0 if pre2 == -1 else dp[i - 1][pre2]

                if min1 == -1 or dp[i][j] < dp[i][min1]:
                    min2, min1 = min1, j
                else:
                    min2 = j
        return dp[len(costs) - 1][min1]
