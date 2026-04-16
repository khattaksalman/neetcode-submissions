# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)

        dummy.next=head
        lenth = 0
        
        curr = head

        while curr != None:
            lenth+=1
            curr=curr.next

        delete = lenth - n
        prev = dummy
        curr = head
        
        i=0
        while i < delete:

            prev=prev.next
            i+=1
        prev.next=prev.next.next

        return dummy.next
