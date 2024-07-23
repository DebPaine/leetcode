class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Time: O(nlogn), since we are sorting the intervals array 
        Space: O(n), if we consider the output array

        Algorithm:
        Not a very difficult problem. We first have to sort the intervals array. We then check if there
        are any overlapping intervals with the previous interval in the output.
        """
        intervals.sort()    # need to sort if for [[1,4], [0,4]]
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            prev_start, prev_end = merged[-1]
            if start <= prev_end:
                merged[-1] = [prev_start, max(prev_end, end)]   # need to take max for [[1,4], [2,3]]
            else:
                merged.append([start, end])
        
        return merged