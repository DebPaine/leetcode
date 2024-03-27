# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Time: O(n), where n is no. of nodes in the tree
        Space: O(n) if tree is LL, O(logn) if tree is balanced

        Algorithm:
        We go through each node using dfs from root to leaf. While traversing, we add the current node.val
        to a string and form a number till we reach the leaf. After reaching the leaf, we convert it back to 
        int and add it to output. We do this for all paths and get the final result.
        """

        output = 0

        def dfs(node, curr):
            nonlocal output
            if not node:  # we still need this condition along with below one since there might be node with either left or right nodes
                return None
            if not node.left and not node.right:  # this means that we are at leaf node
                curr += str(node.val)
                output += int(curr)
                return

            dfs(node.left, curr + str(node.val))
            dfs(node.right, curr + str(node.val))
        
        dfs(root, '')
        return output