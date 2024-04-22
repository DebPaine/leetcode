class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Time: O(n), where n is len(s2)
        Space: O(len(s1)), since we are only storing len(s1) elements in the counts as it's the sliding window length
        
        Algorithm:
        1. We have to get the count of elements of s1
        2. We then have to check for every sw (len(s1)) in s2, are the counts same or not
        3. If the counts are the same, then we can say that permutation of s1 is present in s2, else return False
        """
        sw = len(s1)
        s1_count = Counter(s1)
        sw_count = Counter(s2[:sw])
        if s1_count == sw_count:
            return True

        left = 0
        for right in range(sw, len(s2)):
            sw_count[s2[right]] += 1
            sw_count[s2[left]] -= 1
            if sw_count[s2[left]] <= 0:
                del sw_count[s2[left]]

            if sw_count == s1_count:
                return True
            left += 1
        
        return False