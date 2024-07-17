class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Time: O(n)
        Space: O(n), since we are storing the cleaned string

        Algorithm:
        Easy problem, we just need to clean all the non alphanumeric characters and lowercase the string.
        We then need to use the left and right pointer on either end of the cleaned string and if both the 
        pointers have the same characters or not.
        """
        cleaned_s = "".join([char for char in s if char.isalnum()]).lower()

        l, r = 0, len(cleaned_s) - 1
        while l <= r:
            if cleaned_s[l] != cleaned_s[r]:
                return False
            l += 1
            r -= 1
        
        return True