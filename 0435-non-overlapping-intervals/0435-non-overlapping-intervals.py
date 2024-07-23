class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_end = intervals[0][1]  # we only need to track the prev_end and not prev_start value
        output = 0

        for start, end in intervals[1:]:
            if start < prev_end:    # if there is an overlap
                output += 1
                prev_end = min(prev_end, end)
            else:   # if there is no overlap, then set the prev_end as end
                prev_end = end

        return output 
