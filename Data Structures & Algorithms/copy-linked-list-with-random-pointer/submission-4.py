class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # If the original linked list is empty,
        # there is nothing to copy.
        if not head:
            return None

        # Dictionary stores:
        #
        # ORIGINAL NODE  →  COPIED NODE
        #
        # {None: None} is added so that when curr.next
        # or curr.random is None, map[None] gives None
        # instead of causing a KeyError.
        map = {None: None}

        curr = head

        # ------------------------------------------------
        # PASS 1: Create a copy of every node
        # ------------------------------------------------

        while curr:

            # Create a completely new node with the
            # same value as the original node.
            #
            # If curr is Node(5), this creates Node(5)
            # at a DIFFERENT memory location.
            map[curr] = Node(curr.val)

            # Move to the next original node.
            curr = curr.next

        # At this point, we have:
        #
        # Original:       1 → 2 → 3
        #
        # Dictionary:
        # 1 → 1'
        # 2 → 2'
        # 3 → 3'
        #
        # But the copied nodes are NOT connected yet.

        curr = head

        # ------------------------------------------------
        # PASS 2: Connect next and random pointers
        # ------------------------------------------------

        while curr:

            # Get the copy corresponding to the
            # current original node.
            #
            # If curr = 1,
            # map[curr] = 1'
            copy = map[curr]

            # The original node's next pointer tells us
            # which ORIGINAL node should come next.
            #
            # Example:
            #
            # curr = 1
            # curr.next = 2
            #
            # We don't want:
            # 1'.next = 2       ← WRONG
            #
            # We want:
            # 1'.next = 2'      ← CORRECT
            #
            # map[curr.next] gives us 2'.
            copy.next = map[curr.next]

            # Same idea for the random pointer.
            #
            # Example:
            #
            # curr.random = 3
            #
            # We want:
            # 1'.random = 3'
            #
            # map[curr.random] gives us 3'.
            copy.random = map[curr.random]

            # Move to the next ORIGINAL node.
            curr = curr.next

        # map[head] is the copied version of the
        # original head node.
        #
        # We return the HEAD OF THE COPIED LIST,
        # not the original head.
        return map[head]