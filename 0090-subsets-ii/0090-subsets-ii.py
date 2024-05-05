class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n*2**n) since we are generating all the non-duplicate subsets, and we are copying the subset
        Space: O(n) since we are using the internal call stack

        Algorithm 1:
        Similar to subsets and combinations problem. We have to create non duplicate power sets and return it.
        Note: We are using backtrack(i+1, subset) instead of using backtrack(start+1, subset) to avoid duplicates (?) 

        Algorithm 2:
        This is much easier to understand. It's the same logic as Subsets problem. Here we just sort nums list before
        doing recursion on it. This will allow us to check if the previous value in nums is the same as the current value.
        If the values are the same, then we won't do recursion as it will be redundant and it will generate duplicate subsets.
        Article:
        https://medium.com/@CalvinChankf/a-general-approach-for-subsets-combinations-and-permutations-5c8fe3aff0ae
        """
        # # Algorithm 1
        # nums.sort()
        # output = [] 
        # def backtrack(start, subset):
        #     output.append(subset[:])
        #     if start >= len(nums):
        #         return

        #     for i in range(start, len(nums)):
        #         if i > start and nums[i] == nums[i-1]:
        #             continue
        #         subset.append(nums[i])
        #         backtrack(i + 1, subset)
        #         subset.pop()
        # backtrack(0, [])
        # return output 


        # Algorithm 2
        nums.sort() 
        output = []
        def backtrack(nums, subset):
            output.append(subset)
            if len(nums) == 0:      # this is not really needed as we won't enter the loop if nums is empty
                return

            for i in range(len(nums)):
                if i > 0 and nums[i-1] == nums[i]:
                    continue
                backtrack(nums[i+1:], subset+[nums[i]])

        backtrack(nums, [])
        return output