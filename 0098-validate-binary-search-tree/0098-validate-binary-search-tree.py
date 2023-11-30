# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Time: O(n), where n is the number of nodes in the tree
        Space: O(n), if bst is like LL, else O(logn) if bst is balanced
        
        Instead of comparing current node's val with left and right children, we can just keep updating the 
        lower and upper boundaries of current node's val.
        """
        def dfs(node, lower, upper):
            if not node:  # a null node is a valid BST
                return True
            if not (lower < node.val < upper):  # check the current node's val with lower and upper values
                return False 

            left = dfs(node.left, lower, node.val)   # left child has to be lesser than current node.val
            right = dfs(node.right, node.val, upper) # right child has to be greater than current node.val
            return left and right
            
        return dfs(root, -math.inf, math.inf)