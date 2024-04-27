class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Time: O(n**2), where n is len(nums)
        Space: O(1), if we are not considering output

        Algorithm:
        This is a hard problem as there are a couple of tricky edge cases. We first sort the 
        input array so that we can use two pointers to traverse and decreasing the time complexity.
        We then add up the total of the three pointers and see if it totals to 0. If it does, then 
        we append the numbers to output. We then check if the next numbers are the same or not. If they
        are the same, then we keep iterating till we find a different number. This is because we 
        don't want to add the same triplets in the output again.
        """
        output = []
        nums.sort()     # O(nlogn) time
        
        for i, num in enumerate(nums):
            if nums[i] > 0:     # if nums[i] > 0, we don't have to go further as the next numbers will be greater due to sorted array
                return output
            # i > 0 since for i = 0, we will go over the value for the first time so it's fine
            # if nums[i] == nums[i-1], then there is no point going forward since we will get the same triplet
            if i > 0 and nums[i-1] == nums[i]:  # we can check the previous value is same or not as we have sorted tha array
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = num + nums[l] + nums[r]
                if total == 0:
                    output.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    while l < r and nums[r+1] == nums[r]:
                        r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        
        return output