class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
     #   |   |    |
     #   |   |    |
     #   |    |    |
     #            |
     #            |
     #     
     # condition:i<=j<k
     #           i+j>k  
          #k
     # 2,3,4,4   
     # i j  
        nums.sort()
        length=len(nums)
        output=0

        #nested loop-chck k 3rd element
        for k in range (2, length):
            i,j=0,k-1 #2 pointers
            while i < j:
                if nums[i]+nums[j]>nums[k]: #possible to create
                    output+=(j-i) #length of arr
                    j-=1
                else:
                    i+=1 #till pointers meet in middle
        return output