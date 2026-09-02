# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Create a dummy node.
        # The dummy stays before the actual head of the list.
        #
        # Before:
        # head → 1 → 2 → 3
        #
        # After:
        # dummy → 1 → 2 → 3
        dummy = ListNode(0)

        # Connect the dummy node to the actual head.
        dummy.next = head


        # groupPrev always points to the node
        # RIGHT BEFORE the group we want to reverse.
        #
        # Initially:
        #
        # groupPrev
        #     ↓
        # dummy → 1 → 2 → 3 → 4 → 5
        groupPrev = dummy


        # Keep processing groups until there are
        # fewer than k nodes remaining.
        while True:

            # Start at the node before the current group.
            #
            # Example:
            #
            # groupPrev
            #     ↓
            # dummy → 1 → 2 → 3 → 4 → 5
            kth = groupPrev


            # Move kth forward k times.
            # We are trying to find the LAST node
            # of the current group.
            for _ in range(k):

                # Move one node forward.
                kth = kth.next


                # If kth becomes None, there aren't
                # enough nodes to make a complete group.
                #
                # Example:
                #
                # Remaining nodes: 4 → 5
                # k = 3
                #
                # We cannot reverse this incomplete group.
                if not kth:

                    # Return the beginning of the actual list.
                    # We return dummy.next, NOT dummy.
                    return dummy.next


            # At this point, kth is the LAST node
            # of the group we want to reverse.
            #
            # Example:
            #
            # dummy → 1 → 2 → 3 → 4 → 5
            #         ↑         ↑
            #    groupPrev     kth
            #
            # We want to reverse:
            #
            # 1 → 2 → 3


            # Save the node immediately AFTER
            # the current group.
            #
            # Example:
            #
            # 1 → 2 → 3 → 4 → 5
            #         ↑   ↑
            #        kth groupNext
            #
            # groupNext = 4
            groupNext = kth.next


            # Start the reversal process.
            #
            # We set prev = groupNext instead of None.
            #
            # Why?
            #
            # After reversing:
            #
            # 1 → 2 → 3
            #
            # We want:
            #
            # 3 → 2 → 1 → 4 → 5
            #
            # So node 1 should eventually point to 4.
            prev = groupNext


            # curr starts at the FIRST node
            # of the group we want to reverse.
            #
            # groupPrev → 1 → 2 → 3 → groupNext
            #             ↑
            #            curr
            curr = groupPrev.next


            # Reverse nodes until we reach groupNext.
            #
            # We use groupNext as the stopping point.
            while curr != groupNext:

                # Save the next node BEFORE changing curr.next.
                #
                # Example:
                #
                # curr → 1 → 2
                #
                # nxt becomes 2.
                nxt = curr.next


                # Reverse the pointer.
                #
                # Example:
                #
                # Before:
                #
                # curr → 1 → 2 → 3
                # prev → 4
                #
                # After:
                #
                # 1 → 4
                curr.next = prev


                # Move prev forward.
                #
                # prev now becomes the node
                # we just reversed.
                prev = curr


                # Move curr to the next node
                # that we saved earlier.
                curr = nxt


            # After the reversal finishes:
            #
            # Original:
            #
            # groupPrev → 1 → 2 → 3 → 4
            #
            # Reversed:
            #
            # groupPrev → 1 → 4
            #
            #                 and
            #
            # 3 → 2 → 1 → 4
            #
            # groupPrev is still pointing toward
            # the OLD first node (1).
            #
            # We need to remember this node because
            # it is now the LAST node of the reversed group.


            # Save the old first node.
            #
            # This node will become groupPrev
            # for the next iteration.
            temp = groupPrev.next


            # Connect the previous part of the list
            # to the new first node of the reversed group.
            #
            # kth is the original last node.
            # After reversal, it becomes the first node.
            #
            # Before connecting:
            #
            # groupPrev → 1 → 4
            #
            # and separately:
            #
            # 3 → 2 → 1 → 4
            #
            # After connecting:
            #
            # groupPrev → 3 → 2 → 1 → 4
            groupPrev.next = kth


            # Move groupPrev to the LAST node
            # of the group we just reversed.
            #
            # temp is the old first node.
            #
            # Example:
            #
            # dummy → 3 → 2 → 1 → 4 → 5
            #                  ↑
            #              groupPrev
            #
            # Now the next group starts after this node.
            groupPrev = temp