class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        #everything greater than o/p should be changed to val of o/p
        arr.sort() #sort the array
        length=len(arr) #get length
    
        for i in range(length): #iterate through
            value=round(target/length)  #come up with value that if repeated is close to target
            if arr[i] >= value:
                return value
            else: #remains the same so account for the value i.e
                target=target-arr[i]
                length-=1
        return arr[-1]