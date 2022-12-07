class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sum=0
        i=len(piles)-2 #next to last ie 2nd dlast
        t=len(piles)/3 #div by 3
        j=0
        while (j+1 < t): #runs j times
            sum+=piles[i] #add
            i-=2 #shift 2 down after picking
        return sum