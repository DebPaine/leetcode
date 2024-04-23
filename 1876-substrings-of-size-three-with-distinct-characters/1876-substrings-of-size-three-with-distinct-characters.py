class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        """
        Time: O(n)
        Space: O(1), since the hashmap will need constant space as it will always be sw size

        Algorithm:
        We just have to follow the standard sliding window template and check for every window
        if we have sw unique elements or not.
        """
        sw = 3     
        unique = defaultdict(int)   # will always be of size sw, so constant space is required
        good = 0

        for char in s[:sw]:
            unique[char] += 1
        if len(unique) == sw:
            good += 1
    
        left = 0
        for right in range(sw, len(s)):
            unique[s[right]] += 1
            unique[s[left]] -= 1
            if unique[s[left]] <= 0:    
                del unique[s[left]]
            if len(unique) == sw:   # check if there are sw unique elements in the hashmap
                good += 1
            left += 1

        return good
