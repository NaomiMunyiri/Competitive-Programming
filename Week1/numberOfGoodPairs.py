class Solution:
    #O(n^2)
    #store in dic
    #loop twice
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter=0
        dic={}

        for i in nums:
            if i in dic:
                counter+=dic[i]
                dic[i]+=1
            
            else:
                dic[i]=1
        return counter