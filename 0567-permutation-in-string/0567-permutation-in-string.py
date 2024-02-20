class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Time: O(n), where n is len(s2)
        Space: O(len(s1)), since we are only storing len(s1) elements in the counts as it's the sliding window length
        
        Steps:
        1. We have to get the count of elements of s1
        2. We then have to check for every sw (len(s1)) in s2, are the counts same or not
        3. If the counts are the same, then we can say that permutation of s1 is present in s2, else return False
        """
        s1_count = {}
        s2_count = {}
        sw = len(s1)

        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1
        
        for char in s2[:sw]:
            s2_count[char] = s2_count.get(char, 0) + 1
        
        # Check if the above s1_count and s2_count is the same for the first iteration
        if s1_count == s2_count:
            return True

        for i in range(len(s2)-sw):
            s2_count[s2[i]] -= 1
            if s2_count[s2[i]] == 0:
                del s2_count[s2[i]]
            s2_count[s2[i+sw]] = s2_count.get(s2[i+sw], 0) + 1

            if s1_count == s2_count:
                return True

        return False 