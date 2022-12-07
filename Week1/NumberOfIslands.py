class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #iterate the grid
        height=len(grid)
        width=len(grid[0]) #len at index 0
        count=0

        for i in range (height):
            for j in range (width):
                if grid[i][j]=="1":
                    #count neighbouring 1s
                    self.dfs(grid,i,j)
                    count+=1 #returns number of connecting 1s
        return count

    def dfs(self,grid,i,j):
        #must be within walls of the grid and if grid[i][j]=1
        if i < 0 or i>= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j]!=1:
            return

        grid[i][j]="#" #ensures no repitition of visited ones
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)