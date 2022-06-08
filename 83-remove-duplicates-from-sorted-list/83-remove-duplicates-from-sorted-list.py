# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        b = [] 
        
        cur  = dum =  ListNode()
        while head : 
            if head.val not in b : 
                b.append(head.val)
                cur.next = head
                cur,head = cur.next , head.next 
                cur.next = None 
            else : 
                head = head.next
        return dum.next
                
            

            
        
    
            
        
        
        
            
    
            
        