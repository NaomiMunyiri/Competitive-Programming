class Solution:
    def frequencySort(self, s: str) -> str:
        #use counter object to store number of times it appears
        c=Counter(list(s)) 
        #sort in descending by val of times it appears
        c_list=sorted(c,key=lambda x:c[x],reverse=True)
        output=[]
        for x in c_list:
            #o/p times it appears
            output.append(x*c[x])
        return "".join(output) #generate sring