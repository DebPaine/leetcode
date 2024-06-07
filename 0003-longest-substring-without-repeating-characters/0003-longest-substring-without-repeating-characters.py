class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time: O(n)
        Space: O(26) ~= O(1)

        Algorithm:
        We just have to go through the sliding window and see if we find any duplicates or not
        in the current window. If we find duplicates, we have to iterate till there are no more
        duplicates and carry on with the iteration.
        """
        chars = set()
        output = 0
        l = r = 0

        while l <= r < len(s):
            while s[r] in chars:    # we need to use a loop here for inputs like "qrsvbspk"
                chars.remove(s[l])
                l += 1

            chars.add(s[r])
            output = max(output, len(chars))
            r += 1
        
        return output