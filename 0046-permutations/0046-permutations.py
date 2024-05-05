class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n!)
        Space: O(n)

        Algorithm 1:
        This problem is much easier to solve by visualizing a decision tree. We have to go through nums
        and change the ordering in-place and then add the newly ordered nums to the output. Using backtracking, 
        we can guarantee that there will be no duplicates.

        Algorithm 2:
        Very similar to Combinations and other backtracking problems. Here, we have to get all the possible permutations
        of the given array. For that, we will fix one element and swap the other elements as we go down the decision tree.
        We do this by adding the current element to permutation array and use all the other elements as the input for
        the next level of the decision tree.
        """
        # Algorithm 1
        # output = []
        # def backtrack(start):
        #     if start >= len(nums):
        #         output.append(nums[:])
        #         return
            
        #     for i in range(start, len(nums)):
        #         nums[start], nums[i] = nums[i], nums[start]
        #         backtrack(start + 1)
        #         nums[start], nums[i] = nums[i], nums[start]
        # backtrack(0)
        # return output


        # Algorithm 2
        output = []
        def backtrack(nums, permutation):
            # if len(permutation) == len(nums):     # this won't work as both the permutation is increasing and nums is decreasing
            if len(nums) == 0:
                output.append(permutation)
                return
            
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:], permutation+[nums[i]])

        backtrack(nums, [])
        return output