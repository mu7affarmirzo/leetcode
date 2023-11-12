# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        n = len(head)
        q = n // 2 if n % 2 == 0 else n // 2 + 1
        # temp = head[:q] +
        print(zip(head[:q], head[q:][::-1]))
        for i in zip(head[:q], head[q:][::-1]):
            print(i[0], i[1])
        # for i in head[:q]:




a = Solution()
a = a.reorderList([1,2,3,4,5,6,7])
print(a)