# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Time: O(n), where n is no. of nodes in the tree
        Space: O(m), where m is no. of nodes in the queue
        
        Algorithm: Use BFS to find the closest leaf node to the root node and that will be the min depth
        """
        if not root:
            return 0

        min_depth = 0
        queue = deque([root])

        while queue:
            min_depth += 1
            for _ in range(len(queue)):
                node = queue.pop()
                if not node.left and not node.right:
                    return min_depth
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
        
        return min_depth