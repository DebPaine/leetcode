class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Time: O(n)
        Space: O(n)
        """
        visited = set()
        
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        
        return False