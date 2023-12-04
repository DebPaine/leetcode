class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Time: O(2n)~=O(n), where n is len(nums)
        Space: O(n), since we are using a set
        """
        visited = set(nums)
        output = 0

        for num in nums:
            if (num-1) not in visited:  # start of a sequence
                count = 0
                while (num+count) in visited:
                    count += 1
                output = max(output, count)
        
        return output