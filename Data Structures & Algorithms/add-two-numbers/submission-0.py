class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = 0
        y = 0
        i = 0
        j = 0

        while l1:
            x += int(l1.val) * (10**i)
            l1 = l1.next
            i += 1

        while l2:
            y += int(l2.val) * (10**j)
            l2 = l2.next
            j += 1

        z = x + y
        s = str(z)

        prev = ListNode(int(s[-1]))
        jack = prev

        for k in s[::-1][1:]:
            head = ListNode(int(k))
            prev.next = head
            prev = head

        return jack