# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Time: O(n), where n is the no. of nodes in the tree
        Space: O(n), it will actually be O(max(level_nodes or leaf nodes)) which will be equal to ~O(n/2)

        This problem is same as level order traversal. We just have to reverse the level alternatively before appending 
        to output. The reversing part won't make the time complexity O(n**2) as we are just going through the same level
        twice. So it will be O(level)+O(level) = O(level). Addition of all levels will be O(n), which is total no. of nodes.
        """
        if  root is None:
            return None
        
        output = []
        q = deque([root])
        while q:
            subset = []
            for _ in range(len(q)):
                node = q.pop()
                subset.append(node.val)
                if node.left: q.appendleft(node.left) 
                if node.right: q.appendleft(node.right)
            if len(output)%2 == 0:
                output.append(subset) 
            else:
                output.append(subset[::-1])
        return output