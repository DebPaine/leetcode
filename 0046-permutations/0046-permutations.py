class Solution: 
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n!), since permutation for any number is n! and n is len(nums)
        Space: O(n)
        """
        output = []

        def backtrack(start):
            if start >= len(nums):
                output.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return output