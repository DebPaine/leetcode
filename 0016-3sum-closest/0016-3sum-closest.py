class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Time: O(n**2)
        Space: O(1)
        
        Algorithm:
        This is very similar to 3Sum problem. We just have to find the total which is closest to the target. 
        We can just use the absolute value to find the "distance" between total and target (imagine a number line),
        then we can see if it's smaller than the existing "distance" between total and existing closest or not
        """
        closest = math.inf
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:  # we don't really need this condition but this will help us in going through the duplicates again
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                total = num + nums[l] + nums[r]
                # This formula is important and very simple to understand as we only need to find the total which is closest to our target
                if abs(target-total) < abs(target-closest):
                    closest = total

                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    return total

        return closest
