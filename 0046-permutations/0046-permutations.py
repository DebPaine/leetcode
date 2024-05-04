class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n!)
        Space: O(n)

        Algorithm:
        This problem is much easier to solve by visualizing a decision tree. We have to go through nums
        and change the ordering in-place and then add the newly ordered nums to the output. Using backtracking, 
        we can guarantee that there will be no duplicates.
        """
        output = []

        def backtrack(start):
            if start >= len(nums):
                output.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return output