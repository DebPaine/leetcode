# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Time: O(n), where n is the number of nodes in the tree
        Space: O(n) if tree is LL, else O(logn) is tree is balanced
        """
        balanced = True

        def dfs(node):
            nonlocal balanced 
            # If we complete all the left subtrees and balanced is False and then we go to the 
            # right subtree, we will immediately return 0 and won't do recursion
            if node is None or balanced is False:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # We are checking whether the subtrees are balanced or not
            if abs(left-right) > 1:
                balanced = False

            height = 1 + max(left, right)
            return height
        
        dfs(root)
        return balanced

