class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #sort by loss/gain
        #divide by 2
        costs.sort(key = lambda x:x[0]-x[1])
        length=len(costs)
        half=length//2

        min_sum=sum([a for a,b in costs[:half]])+sum([b for a,b in costs[half:]])

        return min_sum