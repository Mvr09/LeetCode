from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1.val != None:
            lst1 = [l1.val]
        if l2.val != None:
            lst2 = [l2.val]

        while l1.next != None:
            l1 = l1.next
            lst1.append(l1.val)
        while l2.next != None:
            l2 = l2.next
            lst2.append(l2.val)

        num1 = int(''.join(map(str, lst1[::-1])))
        num2 = int(''.join(map(str, lst2[::-1])))

        lstOut = [int(digit) for digit in str(num1 + num2)]
        lstOut = lstOut[::-1]
        NodeOut = ListNode(lstOut[0])
        tempNode = None
        for i in range(len(lstOut)):
            tempNode = ListNode(lstOut[i])
        NodeOut.next = tempNode
        return NodeOut




# Creating test cases
l1 = ListNode(3)
l1.next = ListNode(2)

l2 = ListNode(5)
l2.next = ListNode(2)

Sol = Solution()
Sol.addTwoNumbers(l1,l2)