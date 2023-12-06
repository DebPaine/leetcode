class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Time: O(n**2), where n is len(nums)
        Space: O(1)
        """
        closest = math.inf
        nums.sort()

        for i, num in enumerate(nums):
            l, r = i+1, len(nums)-1
            while l < r:            
                total = num + nums[l] + nums[r]
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    return total
                # This is wrong since we need to update closest with total
                # closest = min(abs(target-closest), abs(target-total))
                if abs(target-total) < abs(target-closest):
                    closest = total

        return closest 