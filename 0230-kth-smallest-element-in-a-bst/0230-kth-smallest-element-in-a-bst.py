# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Time: O(n), where n is no. of nodes in BST
        Space: O(n) if BST is like linked list, O(logn) is BST is balanced

        Algorithm: Inorder traversal 
        """
        kth_smallest = 0
        count = k

        def dfs(node):
            nonlocal kth_smallest, count
            if node is None:
                return None
            
            dfs(node.left)
            if count == 0:
                return None
            kth_smallest = node.val
            count -= 1
            dfs(node.right)

        dfs(root)
        return kth_smallest
