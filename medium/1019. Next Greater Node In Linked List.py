# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head):
        m = 0
        for i in range(len(head)-1, -1, -1):
            if head[i] > m:
                m = head[i]
                head[i] = 0
            else:
                head[i] = m
        # for i in range(len(head)):
        #     for j in range(i+1, len(head)):
        #         if head[j] > head[i]:
        #             head[i] = head[j]
        #             break
        #     else:
        #         head[i] = 0
        return head


a = Solution()
a = a.nextLargerNodes([2,7,4,3,5])
print(a)
