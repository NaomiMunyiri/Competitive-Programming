class Solution:
    #O(n)-sliding window
    def lengthOfLongestSubstring(self, s: str) -> int:
        #use set to add $ rm val
        charSet=set()
        l=0 #pointer
        result=0

        for r in range (len(s)): #right pointer iterates
            while s[r] in charSet: #if duplicate
                charSet.remove (s[l]) #remove leftmost
                l +=1 
            charSet.add (s[r]) #add right most character
            result = max(result, r-l+1)
        return result