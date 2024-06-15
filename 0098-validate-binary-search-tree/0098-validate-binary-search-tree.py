# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Time: O(n), where n is the no. of nodes in the tree
        Space: O(n), if tree is LL, else O(logn) if tree is balanced

        Algorithm:
        Our first thought will be to go down the tree using dfs and compare left and right
        node values with parent node value. But we can't directly access the parent node. So,
        we need to keep track of the lower and upper limit for each node as we go down the tree.
        Essentially, we are just keeping track of the boundary conditions between which the node value is allowed.
        """
        # def dfs(node, lower, upper):
        #     if not node:
        #         return True
        #     if not (lower < node.val < upper):
        #         return False
        #     left = dfs(node.left, lower, node.val)
        #     right = dfs(node.right, node.val, upper)
        #     return left and right
        # return dfs(root, -math.inf, math.inf)

        track = []
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            track.append(node.val)
            dfs(node.right) 
        
        dfs(root)

        for i in range(1, len(track)):
            if track[i] <= track[i-1]:
                return False

        return True




