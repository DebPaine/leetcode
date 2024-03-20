# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Time: O(n), where n is the no. of nodes
        Space: O(n)

        We just go level by level and save the nodes in the same level in a subset array
        """
        if root is None:
            return None

        output = []
        q = deque([root])
        while q:
            subset = []
            for _ in range(len(q)):
                node = q.pop()
                subset.append(node.val)
                if node.left: q.appendleft(node.left)
                if node.right: q.appendleft(node.right)
            output.append(subset)
        return output