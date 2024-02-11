# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        x = []

    
        def inOrder(r, x) : 
            if not r :
                return 
            inOrder(r.left,x)
            x.append(r.val)
            inOrder(r.right,x)
        
        inOrder(root,x)
        return x[k-1]

        
        