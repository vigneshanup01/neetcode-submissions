# ============================================================
# PHASE 1: CREATE THE NODE CLASS
# ============================================================

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        # Store both key and value.
        # We need the key later when removing the LRU
        # node from the dictionary.

        self.prev = self.next = None
        # prev -> points to the previous node
        # next -> points to the next node


# ============================================================
# PHASE 2: INITIALIZE THE LRU CACHE
# ============================================================

class LRUCache:

    def __init__(self, capacity: int):

        self.cap = capacity
        # Maximum number of key-value pairs
        # allowed inside the cache.

        self.cache = {}
        # Dictionary:
        #
        # key -> actual Node
        #
        # Example:
        # {
        #     1: Node(1, 10),
        #     2: Node(2, 20)
        # }
        #
        # This allows us to find any node in O(1).


        self.left, self.right = Node(0, 0), Node(0, 0)
        # Create two dummy nodes.
        #
        # LEFT  = sits before the LRU node
        # RIGHT = sits after the MRU node


        self.left.next = self.right
        self.right.prev = self.left
        # Initially:
        #
        # LEFT <-> RIGHT
        #
        # There are no actual cache nodes yet.


    # ============================================================
    # PHASE 3: REMOVE A NODE
    # ============================================================

    def remove(self, node):

        # Before removing:
        #
        # prev <-> node <-> nxt

        prev = node.prev
        # Get the node immediately before 'node'.

        nxt = node.next
        # Get the node immediately after 'node'.


        prev.next = nxt
        # Skip over 'node' in the forward direction.
        #
        # prev -> node -> nxt
        #
        # becomes:
        #
        # prev -> nxt


        nxt.prev = prev
        # Connect nxt back to prev.
        #
        # Now:
        #
        # prev <-> nxt
        #
        # 'node' is disconnected from the list.


    # ============================================================
    # PHASE 4: INSERT A NODE AS MOST RECENTLY USED
    # ============================================================

    def insert(self, node):

        # We always insert just before RIGHT.
        #
        # This means every newly used node becomes:
        #
        # Most Recently Used (MRU)
        #
        #
        # Before:
        #
        # ... <-> prev <-> RIGHT

        prev = self.right.prev
        # Get the current last real node.

        nxt = self.right
        # RIGHT dummy node.


        prev.next = nxt.prev = node
        # Do two connections:
        #
        # prev.next = node
        #
        # RIGHT.prev = node
        #
        # Conceptually:
        #
        # prev -> node
        # RIGHT <- node


        node.next = nxt
        # node -> RIGHT


        node.prev = prev
        # node <- prev


        # Final result:
        #
        # ... <-> prev <-> node <-> RIGHT
        #
        # 'node' is now the MRU node.


    # ============================================================
    # PHASE 5: GET A VALUE
    # ============================================================

    def get(self, key: int) -> int:

        # Check whether the key exists in the dictionary.
        if key in self.cache:

            node = self.cache[key]
            # Find the node in O(1).
            #
            # Dictionary gives:
            #
            # key -> node


            # Since we just accessed this node,
            # it should become the Most Recently Used node.

            self.remove(node)
            # PHASE 5A:
            # Remove it from its current position.


            self.insert(node)
            # PHASE 5B:
            # Insert it before RIGHT.
            #
            # It is now the MRU node.


            return node.val
            # Return the stored value.


        return -1
        # Key does not exist in the cache.


    # ============================================================
    # PHASE 6: PUT A KEY-VALUE PAIR
    # ============================================================

    def put(self, key: int, value: int) -> None:


        # --------------------------------------------------------
        # PHASE 6A: CHECK IF KEY ALREADY EXISTS
        # --------------------------------------------------------

        if key in self.cache:

            self.remove(self.cache[key])
            # Remove the old node from the linked list.
            #
            # We are going to create a new node
            # with the updated value.


        # --------------------------------------------------------
        # PHASE 6B: CREATE AND STORE THE NEW NODE
        # --------------------------------------------------------

        self.cache[key] = Node(key, value)
        # Create:
        #
        # Node(key, value)
        #
        # Then store:
        #
        # key -> Node
        #
        # inside the dictionary.


        # --------------------------------------------------------
        # PHASE 6C: MAKE IT MOST RECENTLY USED
        # --------------------------------------------------------

        self.insert(self.cache[key])
        # Insert before RIGHT.
        #
        # The new/updated node becomes MRU.


        # --------------------------------------------------------
        # PHASE 6D: CHECK IF CACHE EXCEEDED CAPACITY
        # --------------------------------------------------------

        if len(self.cache) > self.cap:


            # ----------------------------------------------------
            # PHASE 6E: FIND THE LEAST RECENTLY USED NODE
            # ----------------------------------------------------

            lru = self.left.next
            # The first real node is always the LRU.
            #
            # LEFT <-> LRU <-> ... <-> MRU <-> RIGHT


            # ----------------------------------------------------
            # PHASE 6F: REMOVE LRU FROM LINKED LIST
            # ----------------------------------------------------

            self.remove(lru)


            # ----------------------------------------------------
            # PHASE 6G: REMOVE LRU FROM DICTIONARY
            # ----------------------------------------------------

            del self.cache[lru.key]
            # The LRU node must be removed from
            # BOTH data structures.