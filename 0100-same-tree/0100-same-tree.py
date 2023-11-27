# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Time: O(p*q)
        Space: O(p*q) worst case if both the trees are LL, else O(log(p*q) if they are balanced 
        
        The only trick here is to get the three base cases right, otherwise it's easy as we only have to go through the nodes
        """
        def dfs(t1, t2):
            # If t1 and t2 are both None, then they are the same so we return True
            if not t1 and not t2:
                return True
            # If one of them is None, then we return False
            if not t1 or not t2:
                return False
            # If the values don't match, then also we return False
            if t1.val != t2.val:
                return False

            # We go through each node from t1 and t2 recursively and verify the above three conditions
            left = dfs(t1.left, t2.left)
            right = dfs(t1.right, t2.right)

            # We only return True if both left and right subtrees return True
            return left and right

        return dfs(p, q)

            