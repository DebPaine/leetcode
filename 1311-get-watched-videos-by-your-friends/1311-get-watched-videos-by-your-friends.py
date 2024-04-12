class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        """
        Time: O(n**2)
        Space: O(n**2)

        Algorithm:
        This is not a difficult problem, just that the question is not very clear. We have to first create a 
        graph using the friends list. Based on that, we have to do DFS and reach the level of friends for which
        they watched the videos. Then using BFS, we can get the frequencies of the videos watched for the given 
        friends in the required level from the current node. We will then sort the videos first based on views, and
        if the views are same for multiple videos then the use the video names (alphabets) to sort them. 
        """
        graph = defaultdict(list)
        freq = defaultdict(int)

        for i, f in enumerate(friends):
            graph[i].extend(f)

        q = deque([id])
        visited = set([id])
        current_level = 0

        while q:
            for _ in range(len(q)):  # we are going level by level using this for loop 
                node = q.pop()
                if current_level == level:
                    for video in watchedVideos[node]:
                        freq[video] += 1
                for n in graph[node]:   # this loop is to add the neighbours of node to the queue
                    if n not in visited:
                        q.appendleft(n)
                        visited.add(n)
            if current_level == level:  # after we finish iterating over the current level, we can break out of BFS
                break 
            current_level += 1
        
        # x[1] is frequency, x[0] are the letters, we have to sort by frequency first and then by letters if frequencies are same
        sorted_list = sorted(freq.items(), key=lambda x: (x[1], x[0]))  # output will be of format [["A", 1], ["B", 2]]
        return [x[0] for x in sorted_list]
        