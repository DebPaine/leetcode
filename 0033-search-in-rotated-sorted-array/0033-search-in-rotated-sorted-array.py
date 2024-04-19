class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Time: O(logn)
        Space: O(1)

        Algorithm:
        Very similar to problem 153. We are first identifying which half of the array is sorted
        and then going through it and trying to find the target. Either the left or the right half 
        will always be sorted as the pivot will fall in one of the halves, so the other half will
        automatically be sorted.
        Steps:
        1. Check if left (or right) array half is sorted or not.
        2. If it's not sorted, then the other half will definitely be sorted.
        3. Search the other half using binary search for the target.
        """
        l, r = 0, len(nums)-1

        while l <= r:
            mid = r - (r - l)//2
            if target == nums[mid]:
                return mid
            # check if left half is sorted or not
            if nums[l] < nums[mid]:
                if nums[l] <= target <= nums[mid]:  # equal sign here since target can nums[l] or nums[mid]
                    r = mid - 1
                else:
                    l = mid + 1
            # if left half is not sorted, then the right half will automatically be sorted
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1