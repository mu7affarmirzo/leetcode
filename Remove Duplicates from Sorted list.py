# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def remove(self):
        pass

class Solution(object):

    def delete_duplicates(self, head):
        if head is None or head.next is None:
            return head

        target_list = head

        while target_list.next is not None:
            if target_list.val == target_list.next.val:
                target_list.next = target_list.next.next
            else:
                target_list = target_list.next
        return head


# my_list = [1,1,2,3,3,3,4]
#
# sorted_list = Solution.delete_duplicates(head=my_list)

if __name__ == "__main__":
    head, head.next, head.next.next = ListNode(1), ListNode(1), ListNode(2)
    head.next.next.next, head.next.next.next.next = ListNode(3), ListNode(3)
    print(Solution().delete_duplicates(head))
