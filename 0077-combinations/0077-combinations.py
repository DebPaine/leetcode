class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Time: O(k*nCk)
        Space: O(n) if we only consider the recursion implicit stack, else O(nCk) if we consider output

        Algorithm:
        Very similar to subsets problem. Here, the difference is that we append to output only when we have
        k elements in the subarray.
        """
        output = []
        def backtrack(start, combination):
            if len(combination) == k:
                output.append(combination)
                return
            if n == 0:
                return

            for i in range(start, n+1):
                backtrack(i+1, combination + [i])
            
        backtrack(1, [])
        return output