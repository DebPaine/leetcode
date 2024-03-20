# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        Time: O(n), where n is no. of nodes in the tree
        Space: O(n)

        Do level order traversal and take avg of values of every level
        """
        if root is None:
            return None

        output = []
        q = deque([root])
        while q:
            subset = []
            for _ in range(len(q)):
                node = q.popleft()
                subset.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            avg = sum(subset)/len(subset)
            output.append(avg)
        return output