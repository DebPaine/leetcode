class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time: O(n)
        Space: O(n)

        Algorithm:
        This is a classic example of using more space and getting better time complexity in return.
        Instead of using two nested loops to go through each element in the array, we are saving
        the current element in a dict and checking if the complement exists or not.
        """
        complement = {}
        for i, num in enumerate(nums):
            if target - num in complement:
                return [complement[target - num], i]
            complement[num] = i
        