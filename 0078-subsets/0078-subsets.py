class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n*2**n) since we are generating all the non-duplicate subsets, and we are copying the subset
        Space: O(n) since we are using the internal call stack

        Algorithm:
        Similar to subsets and combinations problem. We have to create non duplicate power sets and return it.

        Note: We are using backtrack(i+1, subset) instead of using backtrack(start+1, subset) to avoid duplicates (?) 
        """
        output = [] 

        def backtrack(start, subset):
            output.append(subset[:])
            if start >= len(nums):
                return

            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
            
        backtrack(0, [])
        return output