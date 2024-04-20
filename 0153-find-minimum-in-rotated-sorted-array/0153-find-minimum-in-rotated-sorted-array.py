class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Time: O(logn)
        Space: O(1)

        Algorithm:
        Very similar to the sorted rotated matrix problems, all have the similar pattern. We first check the left
        sorted array if it's sorted or not. If not, then we check the right array which will definitely be sorted.
        We then check with the first element of each array part as it will be the min element.
        """
        l, r = 0, len(nums)-1
        output = math.inf

        while l <= r:
            m = r - (r - l)//2
            if nums[l] < nums[m]: # check if left half is sorted or not
                output = min(output, nums[l])   # since nums[l] will be the first element of the left sorted array
                l = m + 1     # after finding the min, we then check the right sorted array
            else:   # if left half is not sorted, then the right half will definitely be sorted
                output = min(output, nums[m]) # since nums[mid] will be the first element of the right sorted array
                r = m - 1     # after finding the min, we then check the left sorted array
                # break     # can't use break here as nums[mid] won't be the min and there might be smaller left of it (eg: [5,1,2,3,4])
        
        return output