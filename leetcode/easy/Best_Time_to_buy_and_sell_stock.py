class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest_buy = highest_sell = max_dif = this_dif = 0  # index
        prices_len = len(prices)
        while highest_sell < prices_len:
            this_dif = prices[highest_sell] - prices[lowest_buy]
            if this_dif >= 0:
                if this_dif >= max_dif:
                    max_dif = this_dif
                highest_sell += 1
            else:
                lowest_buy = highest_sell
                highest_sell += 1
                this_dif = 0

        return max_dif


print(Solution().maxProfit([7,1,6,7,2,3]))