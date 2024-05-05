class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n*2**n) since we are generating all the non-duplicate subsets, and we are copying the subset
        Space: O(n) since we are using the internal call stack and we don't include the output list (it will be O(2**n) then)

        Algorithm 1:
        Similar to subsets and combinations problem. We have to create non duplicate power sets and return it.
        Note: We are using backtrack(i+1, subset) instead of using backtrack(start+1, subset) to avoid duplicates (?) 

        Algorithm 2:
        This is much easier to understand. We can easily plot the decision tree and see that in every recursive call,
        we are fixing one number then doing recursion on the next numbers. We add the current number to the subset and
        keep recursing till we reach the last number in the list.
        Refer this article:
        https://medium.com/@CalvinChankf/a-general-approach-for-subsets-combinations-and-permutations-5c8fe3aff0ae
        """
        # # Algorithm 1
        # output = [] 
        # def backtrack(start, subset):
        #     output.append(subset[:])
        #     if start >= len(nums):
        #         return

        #     for i in range(start, len(nums)):
        #         subset.append(nums[i])
        #         backtrack(i + 1, subset)
        #         subset.pop()
            
        # backtrack(0, [])
        # return output


        # Algorithm 2
        output = []
        def backtrack(nums, subset):
            output.append(subset)
            if len(nums) == 0:      # this is not needed as we won't enter the loop if nums is empty
                return
            
            for i in range(len(nums)):
                backtrack(nums[i+1:], subset + [nums[i]])

        backtrack(nums, []) 
        return output
