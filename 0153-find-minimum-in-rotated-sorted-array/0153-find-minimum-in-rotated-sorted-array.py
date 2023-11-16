class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        output = math.inf

        while l <= r:
            m = r - (r-l)//2
            if nums[l] < nums[m]:
                output = min(output, nums[l])
                l = m + 1
            else:
                output = min(output, nums[m])
                r = m - 1
        return output