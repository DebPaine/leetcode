class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Time: O(logn), where n is len(nums)
        Space: O(1)
        
        We are basically doing binary search where we are eliminating one half at a time. 
        Instead of the standard binary search of finding some target, we are basically eliminating a half 
        when we know that the half is sorted (is in increasing order). We then continue till we 
        reach a single element and exit the loop. We are eliminating one sorted half at a time since we already
        know that the first element of the sorted half will be the smallest. Also, descending elements in array
        is not possible (given in question) so don't get confused!
        """
        l, r = 0, len(nums)-1
        output = math.inf

        while l <= r:
            m = r - (r-l)//2
            # If left is less than mid, then the left half is sorted and we can eliminate that
            if nums[l] < nums[m]:
                output = min(output, nums[l])
                l = m + 1
            # If left is greater than or equal to mid, then the left half is not sorted and the right half is sorted
            else:  # nums[l] >= nums[r] (equal sign) since in while loop l <= r and we then break out of the loop 
                output = min(output, nums[m])
                r = m - 1
        return output