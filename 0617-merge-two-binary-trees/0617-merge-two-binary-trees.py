# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Time: O(min(m,n)), where m and n are the no. of nodes in root1 and root2. This is because the 
        recursion stops when one subtree is None and the other subtree has nodes.
        Space: O(min(m,n))

        Algorithm:
        The base cases are pretty intuitive. We have to create a new binary tree and not merge into an
        existing one as mentioned in the question.
        """
        # if not root1 and not root2:
        #     return None
        # if not root1 and root2:
        #     return root2
        # if root1 and not root2:
        #     return root1
        
        # Different way of writing the same above base cases
        if not root1:
            return root2
        if not root2:
            return root1

        node = TreeNode(root1.val + root2.val) 
        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)
        return node