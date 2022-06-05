# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        lst = []
        while cur!=None :
            if cur in lst :
                return 1 
            else :
                lst.append(cur)
                cur = cur.next
        return 0
        
        