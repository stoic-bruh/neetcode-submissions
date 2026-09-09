# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        net = head
        while net.next!=None:
            if head.next and head.next.next==None:
                prev = head
            if head.next==None:
                if head==net.next:
                    return
                net.next,head.next = head,net.next
                net,head = head.next,head.next
                prev.next = None
            else:
                head=head.next
            
        
        