class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Time: O(n), where n is len(t)
        Space: O(1)
        """
        ptr1, ptr2 = 0, 0

        while ptr1 < len(s) and ptr2 < len(t):  # check ptr1 and ptr2 since s can be an empty string
            if s[ptr1] == t[ptr2]:
                ptr1 += 1
            ptr2 += 1

        return ptr1 == len(s)