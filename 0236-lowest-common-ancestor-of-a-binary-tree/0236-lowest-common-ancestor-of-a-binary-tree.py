# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Time: O(n), where n is the no. of nodes in the tree
        Space: O(n) if tree is LL, else O(logn) if tree is balanced

        Algorithm:
        1. Search left-right until p or q is found, say it was p.
        2. When p is found, then go to the opposite side of a tree searching for q, we don't search below p
        as we assume that q will be there below it anyway, so p is LCA
        3. If we find q in the opposite subtree, that means that q doesn't exist under p and we have to go up
        the recursion stack till we find the LCA
        """
        if root is None:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right
