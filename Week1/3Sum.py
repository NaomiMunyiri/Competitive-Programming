class Solution:
    #O(N^2)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #use nested loop to check for possible combo
        output=[]
        nums.sort() #prevent dublicates

        for i,a in enumerate(nums):
            if i>0 and a == nums[i-1]: #isnt 1st val & duplicate
                continue
            
            #two sum
            l,r=i+1,len(nums)-1 #use pointers to check sum
            while l < r:
                threeSum=a + nums[l] + nums[r]
                if threeSum>0:
                    r-=1
                elif threeSum<0:
                    l+=1
                else: #=0
                    output.append([a, nums[l], nums[r]]) 
                    l+=1 #update pointer
                    #same val,keep shifting
                    while nums[l]==nums[l-1] and l < r:
                        l+=1
        return output 