class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Time: O(n)
        Space: O(1)

        Algorithm:
        We are using the sorted property of the array to our advantage and using left and right
        pointers to add up and see if it's equal to target or not.
        """
        l, r = 0, len(numbers) - 1

        while l < r:    # no need for equal sign since we don't want to use the same number twice when l == r
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1, r+1]
            if total < target:
                l += 1
            else:
                r -= 1

