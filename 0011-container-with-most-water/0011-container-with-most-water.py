class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)

        Algorithm:
        We have to use two pointer technique for the optimized solution. We use the two
        pointers on either side of the container and move inward towards the center. We
        have to consider the lesser of left and right pointer heights as this will determine
        the height of the entire container, else the water will overflow. We then check if
        either the left or the right pointer height is smaller. Based on that, we just move
        the pointer with the lesser height in hope that we can find a taller height.
        """
        max_area = 0
        l, r = 0, len(height) - 1

        while l < r:
            min_height = min(height[l], height[r])
            max_area = max(max_area, (r-l)*min_height)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
                r -= 1 
        
        return max_area