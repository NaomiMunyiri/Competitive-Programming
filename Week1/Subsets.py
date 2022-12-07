class Solution:
    #recursive-build temp array
    #iterative
    #for loop and add no to each list
    #1,2,3
    #[[] [1] [2] [1,2]]
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output=[[]]
        for n in nums:
            output+=[o + [n] for o in output]
        return output