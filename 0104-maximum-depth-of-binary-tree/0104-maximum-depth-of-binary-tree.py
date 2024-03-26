# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Time: O(n), where n is the no. of nodes in the tree
        Space: O(n) is tree if LL, O(logn) if tree is balanced

        Algorithm:
        We just have to reach the leaf nodes and keep adding one every time we go 
        up the tree. We then take the max(left, right) subtrees and add 1 to it to 
        get the height of the current node.
        """
        if root is None:
            return 0

        left = 1 + self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)
        return max(left, right)