# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Time: O(n), where n is the no. of nodes in the tree
        Space: O(n), if tree is LL else O(logn) if tree is balanced

        We just have to do inorder traversal as it will help us traverse the BST in smallest to largest order 
        """
        smallest = None
        counter = k

        def dfs(node):
            nonlocal smallest, counter
            if node is None:
                return None

            dfs(node.left)  
            # The recursion will stop when counter becomes 0 and smallest won't be updated anymore   
            if counter == 0:
                return None
            smallest = node.val
            counter -= 1
            dfs(node.right)

        dfs(root)
        return smallest
