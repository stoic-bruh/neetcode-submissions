# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for x in lists:
            while x:
                arr.append(x.val)
                x = x.next
        arr = sorted(arr)

        for i in range(len(arr)):
            arr[i] = ListNode(arr[i])
            
        for i in range(len(arr)):
            if i == len(arr)-1:
                arr[i].next = None
            else:
                arr[i].next = arr[i+1]
        if not arr :
            return None
        else:
            return arr[0]