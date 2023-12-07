class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n*2**n) since we are generating all the non-duplicate subsets, and we are copying the subset
        Space: O(n) since we are using the internal call stack

        Eg: nums = [1, 2, 3]
        Write down all the possible subsets of nums: [1], [1,2], [1,2,3] etc. We can see that we have subsets where 
        we will always have 1, always have 2, and always have 3.
        We basically have to create a decision tree: 
        1. Left branch we will add the current num 
        2. Right branch we will add empty list
        Just write down all the subsets of an input list and see what logic we are using. Either we will include
        the current number or we won't. We keep doing this for every number in the input list.
        
        Do note that we are appending to output inside of the base case.
        """
        output = []

        def backtrack(i, subset):
            if i >= len(nums):
                output.append(subset[:]) # O(n)time, make a copy of subset and then append it since it's a reference
                return
            
            # Include the left branch of the decision tree, which means include the current nums[i] 
            backtrack(i+1, subset + [nums[i]])
            # Include the right branch of the decision tree, which means not to include nums[i]
            backtrack(i+1, subset + [])
            return

        backtrack(0, [])
        return output

        