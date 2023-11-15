class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Time: O(log(max(piles))*piles)
        Space: O(1)
        """
        l, r = 1, max(piles)   # l is starting from 1 instead of 0 since k can't be 0
        min_k = max(piles)

        while l <= r:
            k = r - (r - l)//2
            total_h = 0
            for pile in piles:
                total_h += math.ceil(pile/k)
            if total_h <= h:
                min_k = k
                r = k - 1
            elif total_h > h:
                l = k + 1
        
        return min_k