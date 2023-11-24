class DoublyLLNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    """
    Time: O(1) for get() and put() operations
    Space: O(n), since we are using a cache dict

    Steps:
    1. First read the problem carefully. We need to have get() and put() operations in O(1) time. For this, 
    we need a hashmap (for O(1) access) and a doubly LL (to maintain the order of the nodes and to 
    get the LRU).
    2. We need to add two functions: one to remove any node from LL, and one to add the node to MRU.
    3. Whenever we get() a node (if it's available in cache), or we put() a value in cache, we have to remove the node and add to MRU. Even in put() where we can just update the value of the node, we are still 
    removing it since the code is easier and more consistent to work with.
    4. We are checking for capacity after we put() a new node since if we check before adding, then the code 
    becomes tedious. 
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru = DoublyLLNode(0, 0)
        self.mru = DoublyLLNode(0, 0)
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def add_mru(self, node):
        """
        Add the node to MRU
        """
        prev_node = self.mru.prev
        self.mru.prev, node.next = node, self.mru
        prev_node.next, node.prev = node, prev_node
    
    def remove(self, node):
        """
        Remove a node from the LL
        """
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node

    def get(self, key: int) -> int:
        # If key exists, then return the value
        if key in self.cache:
            # Remove the node from the current position and move it to MRU
            curr_node = self.cache[key]
            self.remove(curr_node)
            self.add_mru(curr_node)
            return curr_node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])            
        self.cache[key] = DoublyLLNode(key, value)

        # Move the node to MRU
        self.add_mru(self.cache[key])

        # If len(self.cache) > capacity, then evict LRU node
        if len(self.cache) > self.capacity:
            lru_next = self.lru.next
            del self.cache[lru_next.key]
            self.remove(lru_next)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)