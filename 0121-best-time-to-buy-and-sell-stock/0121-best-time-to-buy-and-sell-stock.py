class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Time: O(n), where n is the len(prices)
        Space: O(1)
        """
        min_price = math.inf
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)  # key here is to find the min price till now, essentially using a pointer to keep track of min_price
            profit = price - min_price  # calculate profit using current day price and min_price
            max_profit = max(max_profit, profit)  # see if this profit is max or not

        return max_profit
