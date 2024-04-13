"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Time: O(n) or O(E+V)
        Space: O(E+V)

        Algorithm:
        The question is not very clear as the input in the problem and the input in the question is different. We
        have to traverse the nodes in the given graph one by one. As we traverse, we have to clone them and store 
        them in a hashmap. This hashmap will allow us to not re-visit the same node again while traversing, and will
        also store the cloned node. As we traverse, we have to keep adding the neighbors to the current cloned node too.
        """
        hashmap = {}

        # def dfs(node):
        #     if node in hashmap:
        #         return hashmap[node]

        #     new_node = Node(node.val)
        #     hashmap[node] = new_node
        #     for nei in node.neighbors:
        #         new_node.neighbors.append(dfs(nei))
        #     # return new_node

        # if not node:
        #     return None
        # else:
        #     dfs(node)
        # return hashmap[node]

        if not node:
            return None

        stack = [node]

        # Traverse the given graph node by node and store the clone in hashmap
        while stack:
            curr = stack.pop()
            if curr not in hashmap:
                hashmap[curr] = Node(curr.val)
            
            for nei in curr.neighbors:  # go through each of the neighbors and traverse them
                if nei not in hashmap:  # basically same as a visited set to not traverse the same node again
                    hashmap[nei] = Node(nei.val)    # add the neighbor to the hashmap
                    stack.append(nei)   # traverse to the next neighbor if it's not in hashmap and we haven't traversed before 
                hashmap[curr].neighbors.append(hashmap[nei])    # add the neighbor to the curr cloned node

        return hashmap[node]



        