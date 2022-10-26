class Solution: 
    def select(self, arr, i):
        # code here 
        return arr[i]
        
    def selectionSort(self, arr,n):
        #code here
        for i in range (n-1):
            smallest_value=i
            for j in range(i+1,n):
                if arr[j]<arr[smallest_value]:
                    smallest_value=j
                    
            x=arr[i]
            arr[i]=arr[smallest_value]
            arr[smallest_value]=x