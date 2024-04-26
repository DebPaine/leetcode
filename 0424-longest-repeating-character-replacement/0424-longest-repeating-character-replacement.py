class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Time: O(n), where n is len(s)
        Space: O(26)~=O(1), as we can only have 26 uppercase alphabets

        Steps:
        1. Either iterate over the string using for or while loop using sliding window technique.
        2. First calculate the length of the sliding window.
        3. Then see what is the count of all characters in the sliding window.
        4. Then check which char occurred max no. of times in the sliding window.
        5. Now find out how many chars we have to replace in the sliding window to make the substring have same letters.
        6. Now see if the no. of replacements is greater than k or not. If it's greater, then move left pointer by one
        and remove one occurence of left char from the sliding window. Else, we can consider this as the longest substring.
        7. Keep iterating through the string by increasing the right pointer by one.
        """
        
        char_count = [0]*26
        longest = 0
        l = r = 0

        while l <= r < len(s):
            char_count[ord(s[r]) - ord('A')] += 1
            max_char = max(char_count)
            sw = r - l + 1
            replacement = sw - max_char

            if replacement > k:
                char_count[ord(s[l]) - ord('A')] -= 1
                l += 1
            else:
                longest = max(longest, sw)
            r += 1
            
        return longest

