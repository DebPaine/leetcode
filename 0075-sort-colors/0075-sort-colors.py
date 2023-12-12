class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Time: O(n), where n is len(nums)
        Space: O(1)

        Dutch National Flag algorithm:
        https://www.youtube.com/watch?v=9pdkbqGwUhs
        1. All values to the left of l pointer should be low values.
        2. All values to the right of r pointer should be high values.
        3. All values from left to mid pointer exclusive are mid values.
        4. All values from mid to high pointer are unknown values.
        We will start by having l and mid pointers at 0, then we will iterate
        over nums and start pushing the low values to the left of l pointer,
        and high values to the right of r pointer. The mid values will automatically be in the middle. We will move the mid values and search for the
        unknown values.

        Do not return anything, modify nums in-place instead.
        """
        # Using counting sort
        # output = []
        # counts = [0]*3
        # for num in nums:
        #     counts[num] += 1
        # for i, count in enumerate(counts):
        #     output.append(count*i)


        # Dutch National Flag algorithm
        l, mid, r = 0, 0, len(nums)-1
        while mid <= r:
            if nums[mid] == 0:
                nums[mid], nums[l] = nums[l], nums[mid]
                l += 1
                mid += 1  # mid pointer will have to move to the next unknown value
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[r] = nums[r], nums[mid]
                r -= 1

        
        





        