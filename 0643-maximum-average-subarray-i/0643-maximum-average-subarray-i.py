class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Time: O(n), where n is len(nums)
        Space:  O(1)
        """
        if k > len(nums):  # k, or sliding window length should not be larger than length of nums
            return -1.0

        curr_sum = max_sum = sum(nums[:k])  # calculate the current sum inside sliding window
        for i in range(1, len(nums)-k+1):
            curr_sum += nums[i+k-1] - nums[i-1]   # add the next element and subtract the previous to current sum
            max_sum = max(max_sum, curr_sum)
            
        return max_sum/k

        