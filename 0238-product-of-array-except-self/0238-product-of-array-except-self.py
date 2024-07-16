class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Algorithm:
        Find prefix sum:
        The prefix of first element will always be 1. We then iterate over nums upto len(nums)-1,
        we don't have to go over the last element to get the prefix. We then keep multiplying the 
        current element with the prefix.

        Find postfix sum:
        We can just reverse nums and use the same logic as finding the prefix. Reversing nums makes it
        easier to understand and calculate the postfixes. Postfix of the last element will always be 1.
        """

        prefix, postfix, output = [1], [1], []

        for num in nums[:len(nums)-1]:
            prefix.append(prefix[-1]*num)
        
        for num in nums[::-1][:len(nums)-1]:
            postfix.append(postfix[-1]*num)

        for a, b in zip(prefix, postfix[::-1]):
            output.append(a*b)
        
        return output