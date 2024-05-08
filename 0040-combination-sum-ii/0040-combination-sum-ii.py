class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Time: O(n*2**n)
        Space: O(n)

        Algorithm:
        Very similar to other backtracking problem. Here, we just have to remember on sorting the input
        array before backtracking as we don't want to have duplicate combinations in the output.
        """
        output = []
        candidates.sort()

        def backtrack(nums, combination):
            if sum(combination) == target:
                output.append(combination)
                return
            if len(nums) == 0 or sum(combination) > target:
                return

            for i in range(len(nums)):
                if i > 0 and nums[i-1] == nums[i]:
                    continue
                backtrack(nums[i+1:], combination + [nums[i]])
            
        backtrack(candidates, [])
        return output