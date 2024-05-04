class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Time: O(n*2**n)
        Space: O(n)

        Very similar to 78. Subsets problem. We have to stop recursion when our sum(subset) == target, and also
        if sum is greater or we have reached the leaf nodes of the decision tree. Also, we can have duplicate 
        values in the subset that add up to target. So, we are doing backtrack(i) and not backtrack(i+1) when we 
        are considering nums[i]. It will keep recursing till we hit the base cases. 

        Note: We are using backtrack(i+1, subset) instead of using backtrack(start+1, subset) to avoid duplicate permutations(?).
        """ 
        output = []

        def backtrack(start, subset):
            if sum(subset) > target:
                return
            if sum(subset) == target:
                output.append(subset[:])
                return

            for i in range(start, len(candidates)):
                subset.append(candidates[i])
                backtrack(i, subset)
                subset.pop()

        backtrack(0, [])
        return output
