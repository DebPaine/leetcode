class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n*2**n) since we are generating all the non-duplicate subsets, and we are copying the subset
        Space: O(n) since we are using the internal call stack
        """
        output = []

        def backtrack(i, subset):
            if i >= len(nums):
                output.append(subset.copy()) # O(n)time, make a copy of subset and then append it since it's a reference
                return
            
            # Include the left branch of the decision tree, which means include the current nums[i] 
            backtrack(i+1, subset + [nums[i]])
            # Include the right branch of the decision tree, which means not to include nums[i]
            backtrack(i+1, subset + [])
            return

        backtrack(0, [])
        return output

        