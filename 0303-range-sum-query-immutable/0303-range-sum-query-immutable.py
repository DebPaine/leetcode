class NumArray:

    def __init__(self, nums: List[int]):
        """
        Time: O(n), where n is len(nums)
        Space: O(n)
        
        Try the following problem next:
        https://leetcode.com/problems/range-sum-query-2d-immutable/
        """
        
        # Extra 0 padding at the start so that p[i-1] doesn't error out
        self.p = [0]*(len(nums)+1)  
        for i in range(1, len(nums)+1):
            self.p[i] = nums[i-1] + self.p[i-1]

    def sumRange(self, left: int, right: int) -> int:
        p_sum = self.p[right+1] - self.p[left]
        return p_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)