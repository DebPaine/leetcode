class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Time: O(n)+O(klogn) ~= O(klogn), where n is len(points)
        Space: O(n), where n is len(points)

        Steps:
        1. Calculate the distances and push them to an array
        2. Convert the distances list into a min heap using heapify
        3. Keep popping the min distance from the min heap and add the points to the output
        4. Return the first k elements of the output as there might be more than one point which has the same distance
        """
        
        counter = k
        distances = []
        output = []

        # O(n) time
        for x, y in points:
            distances.append((self._calculate_distance(x, y), (x, y)))
        
        # O(n) time, it will heapify into a min heap based on the first param in tuple (distance, coordinates)
        heapq.heapify(distances)

        # O(klogn) time
        while counter > 0:  # O(k) time
            output.append(heapq.heappop(distances)[1])  # O(logn) time
            counter -= 1

        return output


    def _calculate_distance(self, x, y):
        distance = (x-0)**2 + (y-0)**2
        return distance