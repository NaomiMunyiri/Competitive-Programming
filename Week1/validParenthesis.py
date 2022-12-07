class Solution:
    #O(n)
    #push when you see open par and pop for close
    #stack and hasmap
    def isValid(self, s: str) -> bool:
        stack=[]
        dict={ ")" : "(" , "}" : "{" , "]" :"["}

        for c in s:
            if c in dict:
                if stack and stack[-1]==dict[c]:#val @top is matching open par;last val added
                    stack.pop() #if there, t is a closeing: pop
                else:
                    return False #dont match/empty
            else:
                stack.append(c) #no closing param
        return True if not stack else False #true is stackis empty