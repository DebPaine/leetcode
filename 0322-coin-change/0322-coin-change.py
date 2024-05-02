class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Time: O(n) with memoization, O(2**n) without
        Space: O(n)

        Algorithm:
        Similar to Climbing Stairs problem where we have to figure out how many denominations can
        add up to the required amount and we have to find the min no. of coins required for it.
        """
        memo = {}

        def dfs(total):
            if total == 0:
                return 0
            if total < 0:
                return -1
            if total in memo:
                return memo[total]

            path_total = math.inf
            for coin in coins:
                path = 1 + dfs(total - coin)
                if path == 0:   # no need to continue this iteration as the total for the path will be less than 0
                    continue
                path_total = min(path_total, path)
                memo[total] = path_total
            return path_total

        min_coins = dfs(amount)
        return min_coins if min_coins != math.inf else -1