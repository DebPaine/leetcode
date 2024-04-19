# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Time: O(logn)
        Space: O(1)

        Algorithm:
        The versions are in a sorted order, so we can use binary search on it. The first 
        bad version we find might not actually be the first one, there might be other bad
        versions before it and so we will search using binary search. Also, we don't need to 
        create a list with all the versions.
        """
        l, r = 0, n-1
        # versions = [i for i in range(1, n+1)]  # memory limit exceeded
        bad = 0

        while l <= r:
            mid = r - (r - l)//2
            if isBadVersion(mid+1):  # +1 since lists are 0-indexed and n is starting from 1
                bad = mid + 1
                r = mid - 1
            else:
                l = mid + 1
        
        return bad
