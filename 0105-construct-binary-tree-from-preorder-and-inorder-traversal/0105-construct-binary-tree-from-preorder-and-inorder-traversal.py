# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Time: O(n), if n is the no. of nodes in the tree
        Space: O(n) whether tree is LL or balanced as we are using additional hashmap to store inorder key: value

        Algorithm:
        1. The first element of preorder during recursive calls will represent the root of the subtree
        2. Then we find the above element in inorder array, this will represent the pivot point where
        all the elements to the left of the pivot will represent the nodes in the left subtree and elements
        to the right will represent elements on the right subtree
        3. We then do recursion based on the pivot point and go through the preorder and inorder arrays and 
        construct the binary tree
        """
        inorder_map = {val: i for i, val in enumerate(inorder)}

        def helper(preorder, inorder):
            if not preorder or not inorder:
                return None
            root = preorder[0]
            # pivot = inorder.index(root)  # inefficient as .index is O(n) operation
            pivot = inorder_map[root]
            root_node = TreeNode(root)
            root_node.left = self.buildTree(preorder[1:pivot+1], inorder[:pivot])
            root_node.right = self.buildTree(preorder[pivot+1:], inorder[pivot+1:])
            return root_node
        
        return helper(preorder, inorder)