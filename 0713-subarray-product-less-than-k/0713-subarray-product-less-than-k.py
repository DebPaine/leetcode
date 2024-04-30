class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        Time: O(2n) ~= O(n)
        Space: O(1)

        Algorithm:
        We have to use sliding window here and see which sliding window's have the product of 
        less than k. We then have to count the number of contiguous subarrays within the window
        add it to the count.
        Note: We use the formula count += r - l + 1 to count the no. of subarrays within the window.
        """
        l = r = 0
        product = 1
        count = 0

        # while l <= r < len(nums):
        #     product *= nums[r]
        #     if product < k:
        #         count += r - l + 1
        #     else:
        #         while product >= k and l <= r:
        #             product /= nums[l]
        #             l += 1 
        #         count += r - l + 1
        #     r += 1
        # return count

        # Reformatted version
        while l <= r < len(nums):
            product *= nums[r]
            while product >= k and l <= r:
                product /= nums[l]
                l += 1 
            count += r - l + 1
            r += 1
        return count