class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        visited = set()

        def backtrack(start, subset):
            if tuple(subset) not in visited:
                output.append(subset[:])
            
            visited.add(tuple(subset))
            if len(subset) >= len(nums):
                return

            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i+1, subset)
                subset.pop()

        backtrack(0, [])
        return output

            