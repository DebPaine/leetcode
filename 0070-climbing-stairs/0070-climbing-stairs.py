class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Recursive approach:
        Time: O(n) with memoization, O(2**n) without memoization
        Space: O(n), since we are using recursion and memo

        Iterative approach:
        Time: O(n)
        Space: O(1)

        Algorithm:
        We use a similar approach to Fibonacci problem, where we either go 1 step or 2 steps in every recursion. 
        
        The iterative approach is basically a Fibonacci series, where we start from 1, 2 instead of 0, 1.
        """
        # # Recursive solution with memoization
        # memo = {}
        # def dfs(steps):
        #     if steps == n:
        #         return 1
        #     if steps > n:
        #         return 0
        #     if steps in memo:
        #         return memo[steps]
        #     memo[steps] = dfs(steps + 1) + dfs(steps + 2)
        #     return memo[steps]
        # return dfs(0)

        # Iterative approach
        if n <= 2:  # since there are 0 ways to go 0 steps, 1 way to go 1 step, and 2 ways to go 2 steps
            return n
        # We are not starting from 0, 1 as we do in normal Fibonacci series since we already have the condition
        # above to take care of this scenario where n <= 2. 
        a, b = 1, 2
        output = 0
        for i in range(3, n+1): # here we are starting from 3 since we have added the condition for n <= 2
            output = a + b
            a = b
            b = output
        return output

