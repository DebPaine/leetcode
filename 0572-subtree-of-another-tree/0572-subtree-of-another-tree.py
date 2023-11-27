# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Time: O(s*t), where s is the no. of nodes in root and t is the no. of nodes in t
        Space: O(max(s,t)) worst case, else O(log(max(s,t)))

        This is an extension of 100. Same Tree problem
        We are first going through each node in root and comparing it with subRoot. We then check if subRoot
        is a subTree of root or not. If it's not, then we go to the left and right subtrees of root and 
        start comparing again with subRoot if it's subtree or not and we keep doing this recursively. 
        """
        # Check all the base cases, it can be simplified but wrote it explicitly for better understanding
        if not root and not subRoot:  # if both root and subRoot are None, then they subRoot is subTree
            return True
        if not root and subRoot:  # if root is None then subRoot can't be a subtree
            return False
        if root and not subRoot:  # if subRoot is None then it is subtree of root since root has None nodes
            return True

        # We use helper function at each node of root to see if subRoot is a subtree or not
        if self.same_tree(root, subRoot):
            return True
        else:
            # If subRoot is not subtree then keep searching left and right subtrees of root
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            return left or right  # return if either left or right subtrees of root have subRoot as subtree

    def same_tree(self, s, t):
        # Same as the Same tree problem, go node by node and see if the values match in both the trees
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        
        left = self.same_tree(s.left, t.left)
        right = self.same_tree(s.right, t.right)
        return left and right
    