# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        second=slow.next
        slow.next=None

        prev=None
        curr=second

        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next

        first=head
        second=prev
        
        while first and second:
            first_next=first.next
            second_next=second.next

            first.next=second
            second.next=first_next

            first=first_next
            second=second_next


        
        
        