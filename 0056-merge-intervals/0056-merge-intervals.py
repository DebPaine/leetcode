class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Time: O(nlogn)
        Space: O(1), not counting the output array

        Algorithm:
        Pretty simple problem. We have to sort the intervals first based on the start values. We then see
        if the current interval's start is less than the previous interval's end. If they are, then we have
        an overlap, else we have separate intervals.
        """
        intervals.sort(key=lambda x: x[0])  # sort the array based on the interval start times
        output = []

        # Method 1: using prev_start and prev_end pointers
        # prev_start, prev_end = intervals[0]
        # for start, end in intervals[1:]:
        #     if start <= prev_end:
        #         prev_end = max(prev_end, end)   # we need max in case of [[1,4], [2,3]]
        #     else:
        #         output.append([prev_start, prev_end])
        #         prev_start, prev_end = start, end
        # output.append([prev_start, prev_end]) 
        # return output

        # Method 2: not using any pointers
        output = [intervals[0]]
        for start, end in intervals[1:]:
            previous_end = output[-1][1]
            if start <= previous_end:  # if current start <= end of previous interval
                output[-1][1] = max(previous_end, end)
            else:
                output.append([start, end])
        return output
