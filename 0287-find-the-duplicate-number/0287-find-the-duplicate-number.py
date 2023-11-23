class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Time: O(n), where n is the length of nums
        Space: O(1)
        
        This problem has two parts: 
        1. First, we have to find the meeting point so that we know that there are duplicates (or a cycle in LL)
        2. Second, we have to find the actual duplicate value (or where the cycle has started)
        """
        slow = fast = 0

        # Find the meeting point
        while nums[fast] and nums[nums[fast]]:   # or while True
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:  # This is meeting point of both pointers, doesn't mean it's the answer
                break

        # Find the actual duplicate after we got the meeting point
        ptr = 0
        while nums[ptr] != nums[slow]:  #  or while True 
            ptr = nums[ptr]
            slow = nums[slow]

        return nums[ptr]
