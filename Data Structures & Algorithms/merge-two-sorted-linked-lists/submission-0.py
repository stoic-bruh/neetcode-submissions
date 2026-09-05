# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None:
            return list2
        if list2==None:
            return list1
        if list1.val>list2.val:
            list1,list2 = list2,list1
        head = list1
        head2= list2

        while head:
            next=head.next
            if head.next == None:
                if head2!=None:
                    head.next = head2
                return list1
            if head2.val<head.next.val:
                head.next=head2
                head=head2
                head2 = next
            else:
                head = head.next
            
            



        