# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Time: O(n), where n is the number of nodes in the tree
        Space: O(n) worst case if tree is LL, else can be O(logn)
        """
        # Check if tree is empty
        if not root:
            return 0

        diameter = 0

        def dfs(node):
            # Return -1 instead of 0 since for a single node, we need height as 0 and not 1
            if not node:
                return -1

            nonlocal diameter
            # Find left and right subtrees heights
            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)
            # Find max diameter. It's basically max height of left + max height of right subtrees
            diameter = max(diameter, left + right)
            height = max(left, right)
            # Return height. When we reach back to the root node, we don't need to capture the return since we are updating the diameter as we go 
            return height
        
        dfs(root)
        return diameter

        

        

        