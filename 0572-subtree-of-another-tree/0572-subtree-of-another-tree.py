# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Time: O(n), where n is no. of nodes in the tree
        Space: O(n) is tree is LL, else O(logn) if tree is balanced

        Algorithm:
        Pretty simple once you think about it intuitively. We first traverse via dfs in 
        root tree and check which node val is equal to subRoot node val. We also check if the 
        subRoot starting from the equal nodes by traversing the tree and subRoot together.
        Note: Understand the base cases for dfs and helper functions as they are intuitive
        """
        def helper(t1, t2): 
            if not t1 and not t2:
                return True
            if not t1 and t2 or t1 and not t2:
                return False
            if t1.val != t2.val:
                return False

            left = helper(t1.left, t2.left)
            right = helper(t1.right, t2.right)
            return left and right


        def dfs(t1, t2):
            if not t1:
                return False
            if not t2:
                return True
            if not t1 and not t2:
                return True

            if t1.val == t2.val and helper(t1, t2):
                return True
            
            left = dfs(t1.left, t2)
            right = dfs(t1.right, t2)
            return left or right

        return dfs(root, subRoot)