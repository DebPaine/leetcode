# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Time: O(n), where n is no. of nodes in the tree
        Space: O(max(width)), as we need to store all the nodes for a given level in a queue

        This is just a BFS
        """
        if root is None:
            return None

        output = []
        queue = deque([root]) 

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop()
                level.append(node.val)
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
            output.append(level) 

        return output
