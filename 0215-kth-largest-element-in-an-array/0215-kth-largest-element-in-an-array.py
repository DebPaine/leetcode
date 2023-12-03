class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Max Heap method:
        Time: O(klogn)
        Space: O(1), as we are updating nums in-place

        Min Heap methods:
        Time: O((n-k)logn)
        Space: O(1)
        """

        # Max Heap method
        # count = k
        # nums = [-num for num in nums]  # O(n) time
        # heapq.heapify(nums)  # O(n) time
        # while count > 1:  # O(k) time
        #     heapq.heappop(nums)  # O(logn) time, pop largest element
        #     count -= 1
        # return -nums[0]  # the first element is the largest element in max heap


        # Min Heap method
        heapq.heapify(nums)  # O(n) time
        # Keep popping the smallest element till we are left with k elements, which will be the k largest ones
        while len(nums) > k:  # O(n-k)
            heapq.heappop(nums)  # O(logn) time, pop smallest element
        return nums[0]  # the first element is the smallest element out of k elements, so overall it's k largest