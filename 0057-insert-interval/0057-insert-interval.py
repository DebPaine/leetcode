class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []

        for i in range(len(intervals)):
            # if end of newInterval is before the start of current interval
            if newInterval[1] < intervals[i][0]:
                output.append(newInterval)
                return output + intervals[i:]
            # if start of newInterval is after the end of current interval
            elif newInterval[0] > intervals[i][1]:
                output.append(intervals[i])     # we are not returning anything here as there may be other overlapping intervals
            # if there is an overlap
            else:
                # we update the newInterval as there maybe other intervals in the next iterations which also merge with this one
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        # this is because there is a chance that the first condition never executes and the newInterval never gets appended to output
        output.append(newInterval) 
        return output
