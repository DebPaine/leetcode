"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        Time: O(n), where n is the no. of nodes in the tree
        Space: O(m), where m is the max size of the queue

        Algorithm:
        We have to do a normal BFS and go level by level here. The trick is to also use the next pointer to 
        traverse the tree.
        """
        if not root:
            return None

        # q = deque([root])
        # while q:
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             node.left.next = node.right  # connect the left and right children of the current node
        #         if node.right and node.next:  # we explicitly don't have to check for node.right since node.left exists
        #             node.right.next = node.next.left  # if next node exists for current node, then traverse it 
        #         if node.left: q.append(node.left)
        #         if node.right: q.append(node.right)
                
        # return root

        # BFS without a queue
        dummy = Node(999999)
        head = root  
        while head:
            prev = dummy
            curr = head
            while curr:
                if curr.left:
                    prev.next = curr.left
                    prev = prev.next
                if curr.right:
                    prev.next = curr.right
                    prev = prev.next
                curr = curr.next
            head = dummy.next
            dummy.next = None
        return root











