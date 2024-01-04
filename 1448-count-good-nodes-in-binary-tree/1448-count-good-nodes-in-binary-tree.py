# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Time: O(n), where n is the number of nodes in the tree
        Space: O(n) if tree is LL, else O(logn) if tree is balanced

        We just have to keep track of the max value from the root node to the current node we are at
        """
        good_nodes = 0

        def dfs(node, max_val):
            nonlocal good_nodes
            if not node:
                return None

            if node.val >= max_val:
                good_nodes += 1

            dfs(node.left, max(max_val, node.val))
            dfs(node.right, max(max_val, node.val))

        dfs(root, -math.inf)
        return good_nodes