# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Time: O(p or q), where p or q are the total no. of nodes in both the tree 
        Space: O(p or q), if tree is linked list else O(logp or logq) if tree is balanced

        Algorithm: The base cases are the main thing and easy to understand, then we just do
        a preorder traversal through both the trees
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right