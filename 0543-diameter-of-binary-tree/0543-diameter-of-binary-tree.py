# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Time: O(n), where n is the no. of nodes in the tree
        Space: O(n), if tree linked list, O(logn) if tree is balanced

        Algorithm: 
        We have to do bottom up approach and calculate height of each subtree from
        and get height of the node. We then add the height of left and right subtrees and calculate
        the diameter of the subtree from the current node. We then keep going up and passing the current
        height and calculating the max diameter till we reach the root node
        """
        diameter = -math.inf

        def dfs(node):
            nonlocal diameter
            if node is None:
                return -1

            left = 1 + dfs(node.left)
            right = 1 + dfs(node.right)
            diameter = max(diameter, left + right)
            height = max(left, right)
            return height
        
        dfs(root)
        return diameter
