# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Time: O(n), where n is the no. of nodes in the tree
        Space: O(n) if tree is LL, O(logn) if tree is balanced

        Algorithm:
        Very similar to diameter of binary tree, where we find the max path for any node where
        we find the length of left and right and then add node.val to it.
        """
        max_path = -math.inf

        def dfs(node):
            nonlocal max_path
            if not node:
                return 0

            left = node.val + max(0, dfs(node.left))
            right = node.val + max(0, dfs(node.right))
            path_sum = left + right - node.val  # subtract node.val as we have already added it to left and right
            max_path = max(max_path, path_sum)
            return max(left, right)  # no need to add node.val as we have already added it to left and right
        
        dfs(root)
        return max_path