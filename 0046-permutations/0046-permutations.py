class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n!), since permutation for any number is n! and n is len(nums)
        Space: O(n)
        """
        output = []

        def backtrack(index):
            if index >= len(nums):
                output.append(nums[:])
                return

            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                backtrack(index+1)
                nums[i], nums[index] = nums[index], nums[i]

        backtrack(0)
        return output