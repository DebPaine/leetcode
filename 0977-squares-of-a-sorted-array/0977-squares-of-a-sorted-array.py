class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Time: O(n)
        Space: O(1), if we don't count the output array

        Algorithm:
        Since the input array is sorted, we can use two pointers to traverse through it and 
        see if the squares of left or right is larger. We then keep appending the larger of 
        left and right num to output and take reverse of it. Instead of squaring the left and
        right num, we can just take the absolute of them and compare.

        Also, note that the right most value of input array is the largest value as the array
        is sorted. We don't know if this applies to squared array since there can be a large
        -ve number on the left pointer whose sqaure is bigger. So, we keep comparing the left and
        right values and see whose square is greater.
        """
        l, r = 0, len(nums)-1
        output = []

        while l <= r:
            if nums[l]**2 < nums[r]**2:
                output.append(nums[r]**2)
                r -= 1
            else:
                output.append(nums[l]**2)
                l += 1
        
        return output[::-1]
