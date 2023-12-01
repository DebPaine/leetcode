class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        Time: O(n-k)*log(n)
        Space: O(n)

        Basically, we convert array into a min heap. Then we keep popping the min element 
        from the heap till we are left with k elements. So, we are left with the top k elements.
        The top element will the smallest element in minHeap which has k largest elements.
        """
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)  # O(n) time, we have to first convert the array into heap first
        # The below lines improve the efficiency since are maintaining a minHeap with size k. Otherwise, 
        # the add method will become inefficient as we would be pushing to the entire nums, and time would be 
        # O(logn) instead of O(logk)
        while len(self.minHeap) > self.k:  # O(n-k)*O(logn)
            heapq.heappop(self.minHeap)  # O(logn) time, pops the min value from the heap
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)  # O(logk) time, since minHeap can only be upto k size
        # Check if the minHeap is size k, else keep popping
        while len(self.minHeap) > self.k:  # O(n-k)*O(logn)
            heapq.heappop(self.minHeap)  # O(logn) time, pops the min value from the heap
        return self.minHeap[0]  # The smallest value of minHeap of size k will be the kthlargest of nums
        # return -self.nums[self.k-1]  # we can't directly index into the minHeap array's kth largest element!


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)