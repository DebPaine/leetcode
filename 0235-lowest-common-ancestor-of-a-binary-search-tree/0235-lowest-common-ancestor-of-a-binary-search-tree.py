# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Time: O(n) if BST is LL, else O(logn) is tree is balanced
        Space: O(1) for iterative approach without stack, else O(n) if BST is LL or O(logn) if it's balanced

        For iterative approach without stack, we don't really need a stack since BST has a defined structure 
        where left child is smaller and right child is smaller than current node. So, traversing it becomes 
        easier and we also don't need backtracking. We can use an explicit stack for iterative approach, but 
        it won't be useful as a stack helps us in keeping track of which nodes to visit next and here in BST, 
        we already know what to visit next as per the given conditions.
        """
        # Recursive DFS
        # if not root:
        #     return None

        # # p < q  or q < p, both can be the inputs
        # if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
        #     return root
        # # If both p and q are smaller than root then we have to go to the left subtree
        # elif p.val <= root.val and q.val <= root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # # If both p and q are greater than root then we have to go to the right subtree
        # elif p.val >= root.val and q.val >= root.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        

        # Iterative DFS (without stack)
        if not root:
            return None

        while root:
            if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
                return root
            # If both p and q are smaller than root then we have to go to the left subtree
            elif p.val <= root.val and q.val <= root.val:
                root = root.left
            # If both p and q are greater than root then we have to go to the right subtree
            elif p.val >= root.val and q.val >= root.val:
                root = root.right
