class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Time: O(n*2**n)
        Space: O(n)

        Very similar to 78. Subsets problem. We have to stop recursion when our sum(subset) == target, and also
        if sum is greater or we have reached the leaf nodes of the decision tree. Also, we can have duplicate 
        values in the subset that add up to target. So, we are doing backtrack(i) and not backtrack(i+1) when we 
        are considering nums[i]. It will keep recursing till we hit the base cases. 
        """
        output = []

        # def backtrack(i, subset):
        #     if sum(subset) == target:
        #         output.append(subset[:])
        #         return
        #     if i >= len(candidates) or sum(subset) >= target:
        #         return
            
        #     backtrack(i, subset + [candidates[i]])  # include the current num as we can have duplicates
        #     backtrack(i+1, subset + [])  # exclude the current num and move to the next one
        #     return
        
        # backtrack(0, [])
        # return output

        # Create a decision tree to understand this. 
        # For eg:
        # We will have 2, then 2,2, then 2,2,2 which will backtrack since it's greater than target
        # Then we will have 2,2,3, etc
        # Then we will go back to 2, then 2,3, 2,3,3, etc
        def backtrack(start, subset):
            if sum(subset) == target:
                output.append(subset[:])
                return

            if sum(subset) > target:
                return

            for i in range(start, len(candidates)):
                subset.append(candidates[i])
                backtrack(i, subset)
                subset.pop()
        
        backtrack(0, [])
        return output