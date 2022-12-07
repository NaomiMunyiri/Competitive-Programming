class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #O(n)-DFS
        #pass lower and upper bounds; supposed to be btwn
        #ie root:lower-inf,upper+inf
        #    1: lower- ...., upper=2
        def dfs(lower,upper,node):
            if not node:
                return True
            elif node.val <= lower or node.val>= upper:
                return False
            else: #go down
                        #lower left                           #lower right
                return dfs(lower,node.val,node.left) and dfs(node.val,upper,node.right)
        return dfs(float('-inf'),float('inf'),root)