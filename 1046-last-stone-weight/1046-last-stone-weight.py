class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Time: O(nlogn), where n is len(stones)
        Space: O(1), not counting stones since it's the input and we are modifying it in-place
        """
        stones = [-stone for stone in stones]
        heapq.heapify(stones)  # O(n) time

        while len(stones) > 1:  # O(n)*O(logn) time
            largest = -heapq.heappop(stones)
            second_largest = -heapq.heappop(stones)
            if largest != second_largest:
                heapq.heappush(stones, -(largest-second_largest))  # O(logn) time
        
        return -stones[0] if stones else 0
            