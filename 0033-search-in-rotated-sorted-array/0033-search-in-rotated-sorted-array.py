class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Time: O(n), where n is len(nums)
        Space: O(1)

        Very similar to problem 153. We are first identifying which half of the array is sorted
        and then going through it and trying to find the target. Either the left or the right half 
        will always be sorted as the pivot will fall in one of the halves, so the other half will
        automatically be sorted.
        """

        l, r = 0, len(nums)-1

        while l <= r:
            m = r - (r-l)//2

            if target == nums[m]:
                return m
            if nums[l] < nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
                    