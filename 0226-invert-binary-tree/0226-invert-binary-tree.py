# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Time: O(n), where n is the number of nodes
        Space: O(n) worst case if tree is linked list, else if it's balanced then it's O(logn) 
        """
        # Recursive DFS
        # if not root:
        #     return None
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root

        
        # Iterative DFS 
        # if not root:
        #     return None
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     node.left, node.right = node.right, node.left
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        # return root


        # Iterative BFS
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
        return root
