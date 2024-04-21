class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Time: O(n), where n is len(s)
        Space: O(n)

        Algorithm:
        We will use sliding window of size p to go through s and compare the element count in the
        window to the element count of p and see if it matches or not. If it matches, then we will
        append the starting point of sliding window to output.
        """
        p_count = Counter(p)
        sw = len(p)
        sw_count = Counter(s[:sw])
        output = [0] if p_count == sw_count else []

        left = 0
        for right in range(sw, len(s)):
            sw_count[s[right]] += 1
            sw_count[s[left]] -= 1
            if sw_count[s[left]] <= 0:
                del sw_count[s[left]]
            left += 1
            
            if sw_count == p_count:
                output.append(left)
            
        return output
