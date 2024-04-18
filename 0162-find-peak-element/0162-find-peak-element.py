class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Time: O(logn)
        Space: O(1)

        Algorithm:
        First try solving using normal brute force. Then try to use binary search to solve this. Not sure
        how we are able to use binary search in an unsorted array, go through this again.
        """
        l, r = 0, len(nums)-1
        
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid - 1
        return l