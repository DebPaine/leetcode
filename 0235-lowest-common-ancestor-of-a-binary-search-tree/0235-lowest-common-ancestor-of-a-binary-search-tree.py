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
        Space: O(n) if tree is LL, O(logn) if tree is balanced

        Algorithms:
        1. General algorithm for LCA in binary trees, not just BST
        We can go down the tree and see if we find node with value p or q

        2. BST algorithm
        We can use the property of BST that left child will be smaller and
        right child will be greater than parent. If both p and q are smaller
        than current node, then we have to go to the left subtree, else go to 
        the right subtree. We will return the current node when we find a split point.
        """
        # General algorithm for LCA for Binary tree, not just BST
        # if not root:
        #     return None
        # if root.val == p.val or root.val == q.val:
        #     return root
        
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)
        # if left and right:
        #     return root
        # else:
        #     return left or right

        # BST algorithm using it's unique properties: left child smaller and right child greater than parent
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root
