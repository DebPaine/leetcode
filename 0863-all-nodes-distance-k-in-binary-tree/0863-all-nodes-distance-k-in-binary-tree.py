# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        Time: O(n), since we are converting tree to a graph and traversing it next
        Space: O(n), since we are using a dict to store the graph and using a queue to traverse

        Algorithm: We need to convert the tree to a graph as we can only move downward in a tree 
        and not in all directions. We also need to find all the nodes which are k distance away 
        from target, these nodes can be above, below, same level, etc from the target node. So,
        working with a graph will be much easier.
        1. Convert tree to graph and represent it using adjacency list
        2. Start on the target node of the graph and traverse using BFS
        3. Keep track of all the visited nodes as we don't want to traverse them again by adding to the queue
        """
        # create a graph from the tree using adjacency list
        graph = collections.defaultdict(list)
        output = []
        q = deque([root])  
        # go through the tree using BFS and fill the adjacency list
        while q:
            for _ in range(len(q)):
                node = q.pop()
                if node.left:
                    graph[node].append(node.left)
                    graph[node.left].append(node)
                    q.appendleft(node.left)
                if node.right:
                    graph[node].append(node.right)
                    graph[node.right].append(node)
                    q.appendleft(node.right)
        
        # go radially outward in all directions from the target node level by level
        level = 0
        visited = set([target])  # keep track of the nodes already visited and don't add it again to the queue
        q = deque([target])
        while q:
            for _ in range(len(q)):
                node = q.pop()
                # check if the required level is reached
                if level == k:
                    output.append(node.val)
                else:
                    for vertex in graph[node]:
                        if vertex not in visited:
                            q.appendleft(vertex)
                            visited.add(vertex)
            level += 1
        return output
