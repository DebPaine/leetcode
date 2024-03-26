# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Time: O(n), where n is the no. of nodes in the tree
        Space: O(n) if tree is LL, O(logn) if tree is balanced
        
        Algorithm:
        Go through the nodes and swap it's children.
        Note: We are not just swapping the children's values, we are also swapping the entire subtrees
        """
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
