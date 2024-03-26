# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        Time: O(n), where n is no. of nodes in the tree
        Space: O(n) if tree is LL, O(logn) is tree is balanced

        Algorithm:
        This is same as finding path sum using a running sum for each path we go through. We then check if
        the running sum is equal to targetSum, and if yes then we append the subset to output.
        Note: subset+[node.val] is basically creating a new list, so when we do subset.append(node.val), it 
        won't affect any other subsets as each of them are different in different stack of the recursion tree.
        """

        output = []

        def dfs(node, current_sum, subset):
            if not node:
                return None
            if not node.left and not node.right and (current_sum+node.val) == targetSum:  # if node is leaf
                subset.append(node.val)  # same thing as how we are adding current_sum+node.val since the sum is trailing the recursion
                output.append(subset)
                return

            dfs(node.left, current_sum + node.val, subset + [node.val])  # add [node.val] to the next stack of recursion
            dfs(node.right, current_sum + node.val, subset + [node.val])  # don't use subset.append as it will affect all subsets in tree

        dfs(root, 0, [])
        return output
