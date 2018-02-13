class Solution(object):
    def lowest_cost(self, sell_list, ref_cap, travel_cost, one_day_cost):
        dp = [[0 for _ in range(len(sell_list))] for _ in range(2)]
        dp[0][0], dp[1][0] = travel_cost, travel_cost + one_day_cost
        for i in range(1, len(sell_list)):
            if ref_cap < sell_list[i]:
                dp[0][i] = min(dp[1][i - 1] + travel_cost, dp[0][i - 1] + travel_cost)
            elif ref_cap == sell_list[i]:
                dp[0][i] = min(dp[0][i - 1] + travel_cost, dp[1][i - 1])
            else:
                dp[0][i] = min(dp[0][i - 1] + travel_cost, dp[1][i - 1] + one_day_cost)
            dp[1][i] = min(dp[0][i - 1], dp[1][i - 1]) + travel_cost + one_day_cost

        return dp[0][len(sell_list) - 1]

s = Solution()
print(s.lowest_cost([10, 7, 20, 19, 13], 7, 14, 10))