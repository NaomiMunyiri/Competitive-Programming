class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sum=0
        i=len(piles)-2
        t=len(piles)/3
        j=0
        while (j+1 < t):
            sum+=piles[i]
            i-=2
        return sum