class Solution:
    def findMin(self, nums: List[int]) -> int:
        #binary search-already sorted
        #min element is like looking for pivot
        length=len(nums)
        l,r=0,length-1

        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]: #pivot is on right side
                l=mid+1 #shift to beginning of sorted side
            else:
                r=mid #pivot on left side
        return nums[l]