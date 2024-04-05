# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        """
        Time: O(n), where n is the no. of nodes in the tree
        Space: O(n), since we are using BFS and we have to store the adjacency list

        Algorithm:
        This is pretty similar to "All nodes distance k in binary tree" problem. We first have to convert
        the tree into an undirected graph. This is because we will also have to traverse upwards from child
        to parent and we can't do that in a tree. Then we have to store this graph in an adjacency list
        and traverse it using BFS to spread the infection to the neighbouring nodes.
        """
        infected = None
        graph = defaultdict(list)
        q = deque([root])

        # Step 1: Convert the tree to undirected graph and store it using adjacency list
        while q:
            for _ in range(len(q)):
                node = q.pop()
                if node.val == start:
                    infected = node
                if node.left:
                    graph[node].append(node.left)
                    graph[node.left].append(node)
                    q.appendleft(node.left)
                if node.right:
                    graph[node].append(node.right)
                    graph[node.right].append(node)
                    q.appendleft(node.right)

        # Step 2: Using the above graph, we can traverse from the infected node radially outward
        minutes = -1  # since at min 0, the first node (infected node) becomes infected
        visited = set([infected])

        q = deque([infected])
        while q:
            for _ in range(len(q)):
                node = q.pop()
                for n in graph[node]:  
                    if n not in visited:
                        q.appendleft(n)
                        visited.add(n)
            minutes += 1
        
        return minutes
