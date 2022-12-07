class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c=Counter(arr)
        N=len(arr)
        n=0 #counting to see if removed enough
        output=0
        for k,v in sorted(c.items(),key=lambda x:-x[1]): #descending order
            n+=v #val to pop
            output+=1
            if n >= (N//2):
                break
        return output