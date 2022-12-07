class Solution:
    def decodeString(self, s: str) -> str:
        #3[a]2[bc]
        #stack
        stack=[]
        currentString=""
        currentCount=0
        #4 observations, what to do when you find them
        for i in s:
            if i == "[":
                stack.append(currentString)
                stack.append(currentCount)
                currentString=""
                currentCount=0

            elif i == "]":
                count=stack.pop() #pop last added val ie 3
                previousString=stack.pop() #in case of 3[a2]
                currentString=previousString + count*currentString

            elif i.isdigit():
                #if large digit ie 200
                #2*10+0=20;20*10+0=200
                currentCount=currentCount*10+int(i)

            else: #character
                currentString +=i #add elements to string
        return currentString