class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force is nested loop to check combos
        #hash table-store val needed to get sum
        #i.e 2,7,11,15 tar-9
        #store 7 as key, 0 as index
        lookup={} #lookuptable-maps input values to output values

        for i in range (len(nums)):
            if nums[i] in lookup: #is val in lookup
                return [lookup[nums[i]],i] #val of nums[i] & index
            else:
                lookup[target-nums[i]]=i #add it to lookup
        return None