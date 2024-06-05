class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        Algorithm 1:
        Time: O(1001), where n is 1001
        Space: O(1001)
        Algorithm:
        This technique is more efficient but will only work if we know the constraints beforehand. Here, we
        just create an array of size max constraint and record how many passengers have gotten on or off at
        any given point. We then go through this array and keep adding/subtracting all the passenger changes
        and see if at any point it exceeds the capacity or not.

        Algorithm 2:
        Time: O(nlogn)
        Space: O(n), since worst case we will have all n elements in min_heap
        Algorithm:
        This is also not very difficult. We need to first sort the trips array on the basis of the start
        locations in ascending order. As we go through the iterations, we keep adding the passengers who will
        have gotten in the car. But we also need to remember that between two start positions, the passengers 
        could have gotten off also, which means that there could be end position between two start positions. 
        So, we would have to remove those passengers and then calculate capacities.
        Note: We have to use a heap to efficiently calculate the end position which is the smallest and closest
        to current starting position. We can also use brute force and use a loop but will be more efficient.

        TL;DR: 
        We just have to keep track of how many passengers are there in the car at any given point (or iteration). We 
        have to do this by adding and remove the necessary passengers and then checking if capacity is exceeded or not. 
        """
        # Algorithm 1, easy solution if we know the constraints beforehand
        # passenger_change = [0]*1001   # we know from_i and to_i is max 1000 beforehand

        # for passengers, from_i, to_i in trips:
        #     passenger_change[from_i] += passengers
        #     passenger_change[to_i] -= passengers

        # curr_passengers = 0
        # for change in passenger_change:
        #     curr_passengers += change
        #     if curr_passengers > capacity:
        #         return False
        # return True


        # Algorithm 2, using heap, if we don't know the constraints beforehand 
        trips.sort(key=lambda x: x[1])  # sort the trips array in ascending order of start
        min_heap = []   # will store (end, passengers)

        curr_passengers = 0
        for passengers, start, end in trips:
            curr_passengers += passengers
            # this method won't work as we can't just decrement passenger count for trips which have not even started yet
            # for curr_pass, _, curr_end in trips:
            #     if curr_end <= start:
            #         curr_passengers -= curr_pass
            
            # for this while loop, since each trip can be pushed and popped from heap only once, so time will be O(2n) instead of O(n*2)
            while min_heap and min_heap[0][0] <= start:
                curr_pass = heapq.heappop(min_heap)[1]
                curr_passengers -= curr_pass

            if curr_passengers > capacity:
                return False
            heapq.heappush(min_heap, (end, passengers))
        return True

            