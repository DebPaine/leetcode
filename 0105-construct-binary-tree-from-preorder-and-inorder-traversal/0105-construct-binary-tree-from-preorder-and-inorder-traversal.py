# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Time: O(n) where n is the len(preorder) or len(inorder) since both are same length
        Space: O(n) due to inorder_map and recursion stack 
        """
        inorder_map = {val: i for i, val in enumerate(inorder)}

        def dfs(p, i):
            if not preorder or not inorder:  # since both lengths of preorder and inorder are the same
                return None

            root = TreeNode(preorder[0])
            # pivot = inorder.index(preorder[0])  # .index is O(n) operation so it's inefficient
            pivot = inorder_map[preorder[0]]
            root.left = self.buildTree(preorder[1:pivot+1], inorder[:pivot])
            root.right = self.buildTree(preorder[pivot+1:], inorder[pivot+1:])
            return root
        
        return dfs(preorder, inorder)
            

