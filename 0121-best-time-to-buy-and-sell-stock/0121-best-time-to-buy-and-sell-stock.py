class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Time: O(n), where n is the len(prices)
        Space: O(1)
        
        Algorithm:
        We can use the standard brute force approach of going through each of the prices and then
        computing what's the max profit. Else, we can use the pointer based approach where we keep
        track of the min price and calculate the max profit against it.
        """
        # Brute force, TLE O(n**2) time
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         profit = prices[j] - prices[i]
        #         max_profit = max(max_profit, profit)
        # return max_profit

        # Optimised, O(n) time
        min_price, max_profit = math.inf, 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
