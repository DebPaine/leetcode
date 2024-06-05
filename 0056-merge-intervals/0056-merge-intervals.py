class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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

        # Method 2
        output = [intervals[0]]
        for start, end in intervals[1:]:
            previous_end = output[-1][1]
            if start <= previous_end:  # if current start <= end of previous interval
                output[-1][1] = max(previous_end, end)
            else:
                output.append([start, end])
        return output
