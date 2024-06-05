class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])  # sort the array based on the interval start times
        output = []

        init_start, init_end = intervals[0]
        for start, end in intervals[1:]:
            if start <= init_end:
                init_end = max(init_end, end)
            else:
                output.append([init_start, init_end])
                init_start, init_end = start, end

        output.append([init_start, init_end]) 
        return output
