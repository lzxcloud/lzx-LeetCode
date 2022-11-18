# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @classmethod
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        resNode = ListNode()
        tens = units = num = 0
        while tens or l1 or l2:
            num = (l1.val if l1.val else 0) + (l2.val if l2.val else 0) + tens
            tens, units = num // 10, num % 10
            resNode.next = ListNode(num)
            resNode, l1, l2 = resNode.next, l1.next if l1 else None, l2.next if l2 else None
        return resNode.next


a = ListNode(1, ListNode(2, ListNode(3)))
b = ListNode(3, ListNode(4, ListNode(6)))

Solution.addTwoNumbers(a, b)



