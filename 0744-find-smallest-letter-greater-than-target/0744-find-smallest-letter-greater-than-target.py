class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        Time: O(logn), where n is the no. of letters in letters list
        Space: O(1)

        Algorithm:
        Very simple problem, the brute force and binary search are quite intuitive. We just
        have to search for the letter which is greater than target. In brute force, since we 
        are iterating from left to right and the letters list is sorted, we break out of the 
        loop when we first encounter a letter larger than target as we don't need to go any
        further. For the binary search approach, we do the same thing but now we take advantage 
        of the sorted property of letters list. So, we take two pointers and search for the smallest
        letter in the letters list which is greater than target.
        """
        # Brute force (this runs without any error O(n) time)
        # smallest = letters[0]
        # for letter in letters:
        #     if letter > target:
        #         smallest = letter
        #         break
        # return smallest

        # Optimized approach (Binary search)
        l, r  = 0, len(letters)-1
        smallest = letters[0]
        while l <= r:
            mid = l + (r-l)//2
            if letters[mid] <= target:  # equal to sign since we only want the letters greater than target
                l = mid + 1
            elif letters[mid] > target:
                smallest = letters[mid]
                r = mid - 1
        return smallest

