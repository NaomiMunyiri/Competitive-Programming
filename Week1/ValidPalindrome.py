class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub("[^a-z|^0-9]","",s.lower()) #regex to ensure op is as wated
        l,r=0,len(s)-1

        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l+=1
                r-=1
        return True