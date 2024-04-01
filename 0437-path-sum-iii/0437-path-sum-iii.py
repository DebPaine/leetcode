# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Brute force DFS:
        Time: O(n**2), as we are doing DFS and then, we are doing another DFS from the current node onwards
        Space: O(n)
        Algorithm: We are going down the tree using DFS. We then do another DFS from every node we reach so that
        we can see if there are any paths from the current node which adds up to targetSum.

        Optimized DFS:

        """
        # Brute force DFS
        output = 0
        def helper(node, curr):
            nonlocal output
            if not node:
                return 0
            if (curr + node.val) == targetSum:
                output += 1
                # return  # we don't have to add return here as we need to keep going down the tree to see if there are other paths
            helper(node.left, curr + node.val)
            helper(node.right, curr + node.val)

        def dfs(node):
            if not node:
                return None
            helper(node, 0)  # we do another DFS from every node we reach
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return output

        # Optimized DFS
