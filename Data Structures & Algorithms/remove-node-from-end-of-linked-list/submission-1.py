# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        fr = head
        while fr.next != None:
            l+=1
            fr = fr.next
        fr = head
        m = l-n+1
        if m == 0:
            if n ==1:
                return None
            else:
                head = head.next
                return head
        while m !=1:
            head = head.next
            m-=1
        if m == 1:
            prev = head
            head = head.next
            nxt = head.next
            prev.next = nxt
        head = fr
        return head
        
        