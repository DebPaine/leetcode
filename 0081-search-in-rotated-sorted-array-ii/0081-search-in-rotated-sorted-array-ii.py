class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Time: O(logn), where n is len(nums)
        Space: O(1)

        Very similar to problem 33 (the first part). Just keep in mind of 
        nums[l] == nums[m] == nums[r] condition. We use this to shrink our search 
        space and continue to the next iteration.
        """
        l, r = 0, len(nums)-1

        while l <= r:
            m = r - (r-l)//2

            if target == nums[m]:
                return True
            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
                continue
            # <= since nums[l] and nums[m] can be duplicates
            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            

        return False