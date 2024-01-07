# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Time: O(n), where n is len(nums)
        Space: O(n) if BST is a Linked List, O(logn) if tree is perfectly balanced
        """
        if not nums:
            return None

        mid = len(nums)//2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[0:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:len(nums)])
        
        return node


