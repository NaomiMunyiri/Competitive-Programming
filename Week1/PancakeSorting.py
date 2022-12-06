class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(end):
            start=0
            while start<end:
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1
        N=len(arr)
        output=[]
        for i in range(N-1,-1,-1):
            max_index=i
            for j in range(i,-1,-1):
                if arr[j]>arr[max_index]:
                    max_index=j
            if max_index!=i:
                flip(max_index)
                flip(i)
            output.append(max_index+1)
            output.append(i+1)
        return output