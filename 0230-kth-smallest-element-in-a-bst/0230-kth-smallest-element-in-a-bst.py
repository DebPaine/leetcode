# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Time: O(n), where n is no. of nodes in the tree
        Space: O(n) if tree is LL, O(logn) if tree is balanced

        Algorithm:
        We can use inorder traversal to find the k-smallest elements in a BST.
        """
        counter = k
        output = None

        def dfs(node):
            nonlocal counter, output
            if not node:
                return None
            
            dfs(node.left)
            if counter < 1:
                return None
            output = node.val
            counter -= 1
            dfs(node.right)

        dfs(root)
        return output