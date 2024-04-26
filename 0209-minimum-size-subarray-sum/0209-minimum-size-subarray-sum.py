class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)

        Algorithm:
        This is an easy problem. The intuition is that we will use a sliding window and calculate the
        running sum and compare it with target. If we reach a running sum which is >= target, then we 
        will keep decreasing the window size till running sum is less than target.
        """
        l = r = 0
        current_sum = 0
        min_length = math.inf

        while l <= r < len(nums):
            current_sum += nums[r]
            while current_sum >= target:    # we will decrease the current sum till it's less than the target
                min_length = min(min_length, r - l + 1)
                current_sum -= nums[l]
                l += 1
            r += 1
            
        return min_length if min_length != math.inf else 0
