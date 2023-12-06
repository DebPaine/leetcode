class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n**2), where n is len(nums)
        Space: O(1), if we are not considering output
        """
        output = []
        nums.sort()  # O(nlogn) time

        for i, num in enumerate(nums):
            # i > 0 since for i = 0, we will go over the value for the first time so it's fine
            # if nums[i] == nums[i-1], then there is no point going forward since we will get the same triplet
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                total = num + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    output.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        
        return output