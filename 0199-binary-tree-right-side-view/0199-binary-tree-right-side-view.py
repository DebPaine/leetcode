# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return root
        
        output = []
        queue = deque([root])
        
        while queue:
            right_side_val = None
            for _ in range(len(queue)):
                node = queue.popleft()
                right_side_val = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(right_side_val)
        
        return output