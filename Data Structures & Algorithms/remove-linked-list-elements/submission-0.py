# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        phead =ListNode(0)

        phead.next=head
        prev=phead
        curr =head

        while curr is not None:
            if curr.val == val:
                prev.next=curr.next

            else:     
                prev=curr

            curr=curr.next

        return phead.next    