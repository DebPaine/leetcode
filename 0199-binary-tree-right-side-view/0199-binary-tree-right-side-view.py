# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Time: O(n), where n is the no. of nodes in the tree
        Space: O(n), or O(level with max nodes) ~= O(n/2) ~= O(n)
        Algorithm: Do BFS and take the last element of each level and append it to output
        """
        if root is None:
            return None

        output = []
        q = deque([root])
        while q:
            last_element = 0
            for _ in range(len(q)):
                node = q.pop()
                last_element = node.val
                if node.left: q.appendleft(node.left)
                if node.right: q.appendleft(node.right)
            output.append(last_element)
        return output