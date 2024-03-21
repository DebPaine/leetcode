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
    def connect(self, root: "Node") -> "Node":
        """
        BFS using queue:
        Time: O(n), where n is no. of nodes in tree
        Space: O(n)
        Algorithm: We go level by level and we are basically forming a linked list out of the nodes in each level. Dummy node is used 
        to iterate over the nodes and for the connection

        BFS without using queue:
        Time: O(n), where n is no. of nodes in tree
        Space: O(1)
        Algorithm: It might seem tricky initially but it's not that difficult. We have to use a couple of pointers to keep track of
        our position : head pointer to keep track of the leftmost node of a level, prev pointer for dummy node to traverse through 
        the level. Dummy node will be used to connect the nodes in the same level. To move to the next level, we have to use the
        dummy.next node as it will always point to the level below our current one.
        """
        if root is None:
            return None

        # # BFS using queue
        # q = deque([root])
        # dummy = Node(-100000)
        # while q:
        #     curr = dummy
        #     for _ in range(len(q)):
        #         node = q.pop()
        #         curr.next = node
        #         curr = node
        #         if node.left:
        #             q.appendleft(node.left)
        #         if node.right:
        #             q.appendleft(node.right)
        #     dummy.next = None
        # return root

        # BFS without using queue
        head = root  # pointer to keep track of the leftmost node in a level
        dummy = Node(-100000)
        while head:
            curr = head  
            prev = dummy  # prev pointer to iterate through each level
            while curr:
                if curr.left:
                    prev.next = curr.left
                    prev =  prev.next
                if curr.right:
                    prev.next = curr.right
                    prev = prev.next
                curr = curr.next  # traverse the level left to right
            # Below line will cause a bug where head node doesn't have any children
            # head = head.left if head.left else head.right
            # dummy.next will be the starting point of the next level below current one
            # as we are using dummy for curr.left and curr.right nodes
            head = dummy.next
            dummy.next = None
        return root

                