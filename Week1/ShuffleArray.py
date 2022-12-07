import random  #helps with shuffling
class Solution:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.org=self.nums[:]  #original array
        

    def reset(self) -> List[int]:
        self.nums=self.org[:]  #resets to original
        return self.nums
        

    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums