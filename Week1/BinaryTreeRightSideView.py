class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #lookup table storing height of tree as key
        #Depth First Search
        l=defaultdict(list)

        def dfs(node,height):
            if not node:
                return
            l[height].append(node.val) #append node val as list
            dfs(node.left,height+1) #run dfs on left & ad height
            dfs(node.right,height+1) #run dfs on right & ad height
        dfs(root,0) #run dfs on root, start with 0

        #last node is right mose for each key
        return [v [-1] for k,v in sorted(l.items())] #