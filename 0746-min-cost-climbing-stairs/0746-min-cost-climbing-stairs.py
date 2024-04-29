class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Time: O(n) with memoization, O(2**n) without memoization
        Space: O(n)
        """
        memo = {}

        def dfs(step):
            if step >= len(cost):
                return 0    # we don't need to return anything here as we are calculating the path cost after returning
            if step in memo:
                return memo[step]
            
            left = cost[step] + dfs(step + 1) 
            right = cost[step] + dfs(step + 2) 
            memo[step] = min(left, right)
            return memo[step]

        return min(dfs(0), dfs(1))   # for starting at 0th and 1st step, the output for dfs(1) will already be saved in memo from dfs(0)
