class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Time: O(klogn)
        Space: O(n)

        Steps:
        1. Calculate the distances and create a hashmap mapping the distances to the points
        2. Convert the distances list into a min heap using heapify
        3. Keep popping the min distance from the min heap and add the points to the output
        4. Return the first k elements of the output as there might be more than one point which has the same distance
        """
        output = []
        distance_map = {}
        counter = k

        for x, y in points:  
            d = x**2 + y**2  # we don't really need to take sqrt since if a**2 > b**2, then a > 2
            if d not in distance_map:
                distance_map[d] = []
            distance_map[d].append([x, y])

        distances = list(distance_map.keys())  # distances will be a list of list
        heapq.heapify(distances)  # O(n) time, min heap
        
        while counter > 0 and distances:  # O(k) time, check distances also as it might become empty since we are popping
            smallest = heapq.heappop(distances)  # O(logn)
            output.extend(distance_map[smallest]) # O(len(distance_map[smallest])) time, will concat the k smallest distances
            counter -= 1

        return output[:k]

