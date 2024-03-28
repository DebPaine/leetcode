# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Time: O(n), where n is the no. of nodes in the tree
        Space: O(n) or O(max_level nodes)

        Algorithm:
        We basically have to assign an index for every node in the tree: left children 2*i and right children 2*i+1. 
        We then traverse level by level using BFS, and we then take the last element and first element in the level 
        and it's indexes' difference to calculate the width of the level. We used an array for the q since we can't index
        directly in a deque but we never pop element from the start of the array as it would be O(n) time. So, we populate 
        level by level and we assign it to the queue after we go through the level, so no need to pop anything.
        Note: we have to use 2*i and 2*i+1 for node index since each level will 
        """
        max_width = 0
        q = [(root, 0)]  # we have to use an array instead of a deque so that we can index first and last element in the level

        while q:
            max_width = max(max_width, q[-1][1] - q[0][1] + 1)
            level = []
            for node, i in q:
                if node.left: 
                    level.append((node.left, 2*i))
                if node.right: 
                    level.append((node.right, 2*i+1))
            q = level 
        return max_width