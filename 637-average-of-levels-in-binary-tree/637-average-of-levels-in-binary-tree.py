# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=[]
        result = []
        if (root) :
            q.append(root)
        while q :
            temp = []
            total = 0
            size = len(q)
            for i in range(size) :
                cur = q.pop()
                total+=cur.val
                if cur.left :
                    temp.append(cur.left)
                if cur.right :
                    temp.append(cur.right)
            result.append(total/size)
            while temp:
                q.append(temp.pop())
        return result
            
            

 