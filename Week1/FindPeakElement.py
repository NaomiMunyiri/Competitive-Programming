class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #binary search
        #look for middle
        length=len(nums)
        l,r=0,length-1

        while l<r:
            mid=(l+r)//2
            if nums[mid]<nums[mid+1]: #if mid < next val,peak on right 
                l=mid+1
            else:
                r=mid
        return l