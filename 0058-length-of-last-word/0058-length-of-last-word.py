class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Time: O(n), where n is len(s)
        Space: O(1)
        """
        # l, r = 0, 0
        # max_len = 0

        # while l <= r < len(s):
        #     if s[r] != ' ':
        #         curr_len = r - l + 1
        #         # Since we have to only get the length of last word
        #         max_len = curr_len
        #         r += 1
        #     else:
        #         r += 1
        #         l = r
        # return max_len

        # Alternative
        return len(s.split()[-1])