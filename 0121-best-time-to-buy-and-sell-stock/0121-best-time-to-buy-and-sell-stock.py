class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force, TLE
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         profit = prices[j] - prices[i]
        #         max_profit = max(max_profit, profit)
        # return max_profit

        min_price, max_profit = math.inf, 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
        