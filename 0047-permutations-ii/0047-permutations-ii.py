class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n!)
        Space: O(n) if we don't include the output array, else O(n!)

        Algorithm:
        Very similar to Subsets II problem. Here, we have to remember to sort the input array so that 
        we can check whether the previous value is same as current. If it's same, then we skip the current
        value's recursion tree as it will generate redundant permutations.
        """
        output = []
        nums.sort()

        def backtrack(nums, permutation):
            if len(nums) == 0:
                output.append(permutation)
                return

            for i in range(len(nums)):
                if i > 0 and nums[i-1] == nums[i]:
                    continue
                backtrack(nums[:i]+nums[i+1:], permutation+[nums[i]])
        
        backtrack(nums, [])
        return output