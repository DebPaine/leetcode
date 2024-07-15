class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time: O(n)
        Space: O(n)
        """
        if len(s) != len(t):
            return False

        s_count = Counter(s)
        t_count = Counter(t)
        if s_count == t_count:  # comparing two dictionaries takes O(n) time
            return True
        
        return False