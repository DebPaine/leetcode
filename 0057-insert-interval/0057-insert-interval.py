class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Time: O(n)
        Space: O(n), if we include the output array

        Algorithm:
        This problem seems easy but it's actually difficult to get the conditions right. We have to think about this
        step by step:
        1. Iterate through each of the intervals one by one.
        2. For each interval, we compare it with the newInterval with the below conditions.
        3. If the first two conditions don't execute, that means there is an overlap between newInterval and the current
        interval. Hence, we save this new merged interval in newInterval itself so that in the next iterations we can use it
        and see if there are any other further overlaps or not.
        4. At the end, we append newInterval before returning the output since there is a chance we never return from within 
        the first condition in the loop.
        """

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
