class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeat = set()
        l = r = 0
        output = 0
        
        while l <= r < len(s):
            if s[r] not in repeat:
                output = max(output, r - l + 1)
                repeat.add(s[r])
            else:
                while l <= r and s[r] in repeat:
                    repeat.remove(s[l])
                    l += 1
                repeat.add(s[r])
            r += 1

        return output
