# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Brute force DFS:
        Time: O(n**2), as we are doing DFS and then, we are doing another DFS from the current node onwards
        Space: O(n)
        Algorithm: We are going down the tree using DFS. We then do another DFS from every node we reach so that
        we can see if there are any paths from the current node which adds up to targetSum.

        Optimized DFS:
        Time: O(n), where n is the no. of nodes
        Space: O(n) if tree is LL, else O(logn) if tree is balanced
        Algorithm: We use concept of prefix sum/complement to optimize our approach. We use the formula (curr-target) to see if 
        we have a previous value in the current path already present in the cache. If it is present, then it means that
        there is a path that exists which adds up to target
        """
        # Brute force DFS
        # output = 0
        # def helper(node, curr):
        #     nonlocal output
        #     if not node:
        #         return 0
        #     if (curr + node.val) == targetSum:
        #         output += 1
        #         # return  # we don't have to add return here as we need to keep going down the tree to see if there are other paths
        #     helper(node.left, curr + node.val)
        #     helper(node.right, curr + node.val)

        # def dfs(node):
        #     if not node:
        #         return None
        #     helper(node, 0)  # we do another DFS from every node we reach
        #     dfs(node.left)
        #     dfs(node.right)
        
        # dfs(root)
        # return output

        # Optimized DFS
        output = 0
        cache = {0: 1}  # if root node is 10 and target is 10, then 10-10=0, which means that root node itself can be a valid path

        def dfs(node, curr):
            nonlocal output
            if not node:
                return 0
            curr += node.val
            # if curr == targetSum:  # we can use this also instead of initializing cache = {0: 1}
            #     output += 1
            if (curr - targetSum) in cache:  # we check in cache if the complement value exists, which means there are valid paths
                output += cache[curr - targetSum]
            
            cache[curr] = cache.get(curr, 0) + 1
            dfs(node.left, curr)
            dfs(node.right, curr)
            cache[curr] -= 1  # we are subtracting the frequency of curr from cache since we now go to a different path

        dfs(root, 0)
        return output

