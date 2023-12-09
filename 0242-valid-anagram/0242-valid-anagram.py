class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time: O(n), where n is len(s) or len(t)
        Space: O(n), since we are using hashmaps to store the counts
        """
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}

        for char in s:
            s_count[char] = 1 + s_count.get(char, 0)

        for char in t:
            t_count[char] = 1 + t_count.get(char, 0)

        # This is long form on how to compare two dictionaries of same length
        # for char in s:
        #     if char not in s_count or char not in t_count:        
        #         return False
        #     if s_count[char] != t_count[char]:
        #         return False

        # This is short form on how to compare two dictionaries
        if s_count != t_count:
            return False

        return True 