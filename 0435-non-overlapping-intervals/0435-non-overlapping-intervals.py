class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Time: O(nlogn)
        Space: O(1)
        
        Algorithm:
        Pretty similar to merge intervals problem. We need to first sort the intervals array. We then 
        keep track of the prev_end as we have to know when the previous interval ends. We then check if
        there is an overlap between the current and the previous interval. If there is, then we choose to 
        remove the longer of the two interval as then there would be less chance of overlap with the next
        interval. This is also because we have to find the min no. of intervals that we need to remove.
        """
        intervals.sort()
        prev_end = intervals[0][1]  # we only need to track the prev_end and not prev_start value
        output = 0

        for start, end in intervals[1:]:
            if start < prev_end:    # if there is an overlap
                output += 1
                prev_end = min(prev_end, end)   # we remove the interval which is the longer of the current and previous
            else:   # if there is no overlap, then set the prev_end as end
                prev_end = end

        return output 
