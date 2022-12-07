class Solution:
    #ie leetcode -> 0
    #brute-pointer,check char in 0 check if it exists,continue if so
    #use hash map
    #iterate once, create map to record times it appears
    def firstUniqChar(self, s: str) -> int:
        length=len(s)

        counter=Counter(list(s)) #counter obj, pass list, count times

        for i in range (len(s)):
            if counter.get(s[i])==1: #retrieve val of char in str
                return i
        return -1