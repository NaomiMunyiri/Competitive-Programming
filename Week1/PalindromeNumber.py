class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        d=0
        rev=0
        while x > 0:
            d=x%10  #used to extract last digit ie 151% 10 ->1
            rev=rev*10+d
            x=x//10 #used to find quotirent afer division #151//10 ->15
        if num==rev:
            return True
        else:
            return False