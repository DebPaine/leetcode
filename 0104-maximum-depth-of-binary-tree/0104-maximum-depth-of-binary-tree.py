# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Time: O(n), where n is the number of nodes in the tree
        Space: O(n) worst case if tree is linked list, else O(logn) for balanced binary tree
        """
        # Recursive DFS
        # if not root:
        #     return 0
        # left = 1 + self.maxDepth(root.left)
        # right = 1 + self.maxDepth(root.right)
        # return max(left, right)


        # Iterative DFS
        # if not root:
        #     return 0
        # stack = [(root, 1)]
        # max_depth = 0
        # while stack:
        #     node, depth = stack.pop()
        #     max_depth = max(max_depth, depth)
        #     if node.right:
        #         stack.append((node.right, depth + 1))
        #     if node.left:
        #         stack.append((node.left, depth + 1))
        # return max_depth


        # Iterative BFS
        # if not root:
        #     return 0
        # queue = deque([root])
        # max_levels = 0
        # while queue:
        #     max_levels += 1
        #     for _ in range(len(queue)):
        #         node = queue.pop()
        #         if node.left:
        #             queue.appendleft(node.left)
        #         if node.right:
        #             queue.appendleft(node.right)
        # return max_levels


        # Alternative Iterative BFS
        if not root:
            return 0
        queue = deque([(root, 1)])
        max_level = 0
        while queue:
            node, level = queue.pop()
            max_level = max(max_level, level)
            if node.left:
                queue.appendleft((node.left, level + 1))
            if node.right:
                queue.appendleft((node.right, level + 1))
        return max_level