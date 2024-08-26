"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        b = [] 
        
        def dfs(root):
            if root is None:
                return 
            for i in root.children : 
                dfs(i)
                
            b.append(root.val)
        dfs(root)
        
        return b
        