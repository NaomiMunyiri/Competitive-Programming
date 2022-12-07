class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #does it have same no of oach char
        dic_val={} #create dic
        for x in s: #loop through dic..how many times does it appear
            if x in dic_val:
                dic_val[x]+=1
            else:
                dic_val[x]=1

        for x in t: #is t in dic
            if x in dic_val:
                dic_val[x]-=1 #should wnd up at 0
            else:
                return False
        for value in dic_val.values():
            if value !=0:
                return False
        return True