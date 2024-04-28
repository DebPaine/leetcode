class Solution:
    def fib(self, n: int) -> int:
        """
        Recursive solution:
        Time: O(2**n), without memoization we can visualize this using a tree as we are exponentially generating new nodes, 
        O(n) with memoization
        Space: O(n), since we are using recursive stack and memoization

        Iterative solution:
        Time: O(n), since we are just using a loop
        Space: O(1)

        Algorithm:
        The recursive structure forms a tree structure where left branch is f(n-1) and right branch is
        f(n-2). We can optimize the time complexity by using memoization (by using extra space). 
        
        The iterative approach is done by using a loop to compute the sum of previous two numbers.
        """
        # # Recursive approach with Memoization
        # memo = {}
        # def dfs(n):
        #     if n <= 1:
        #         return n
        #     if n in memo:
        #         return memo[n]
            
        #     memo[n] = dfs(n-1) + dfs(n-2)
        #     return memo[n]
        # return dfs(n)

        # Iterative solution
        if n <= 1:
            return n
        a, b = 0, 1
        output = 0
        for num in range(2, n+1):
            output = a + b
            a = b
            b = output

        return output
            