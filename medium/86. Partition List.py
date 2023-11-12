# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lnode = ldummy = ListNode(0)
        rnode = rdummy = ListNode(0)
        while head:
            if head.val < x:
                lnode.next = ListNode(head.val)
                lnode = lnode.next
            else:
                rnode.next = ListNode(head.val)
                rnode = rnode.next
            head = head.next
        lnode.next = rdummy.next

        return ldummy.next


a = Solution()
a = a.partition([1,4,3,0,2,5,2], 3)
print(a)