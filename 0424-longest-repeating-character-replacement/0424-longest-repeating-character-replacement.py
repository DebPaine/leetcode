class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = [0]*26
        output = 0

        l = 0
        for r in range(len(s)):
            sw_len = r - l + 1
            char_count[ord(s[r]) - ord('A')] += 1
            replacement = sw_len - max(char_count)

            if replacement > k:
                char_count[ord(s[l]) - ord('A')] -= 1
                l += 1
            else:
                output =  max(output, sw_len)
        
        return output