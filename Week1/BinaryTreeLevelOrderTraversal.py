# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #iterate l->r appending to next level
        if root is None:
            return []
        queue=[root] #current level
        next_queue=[] #should hold children
        level=[] #stores values
        result=[]
        while queue != []:
            for root in queue:
                level.append(root.val) #append val of root to level
                if root.left is not None: #check for children
                    next_queue.append(root.left) #append to next q
                if root.right is not None:
                    next_queue.append(root.right)
            result.append(level) #append level to result
            level=[]
            queue=next_queue
            next_queue=[]
        return result

        #queue=[] next_queue=[], level=[], result=[[1],[2,3],[4,5,6,7]]
        