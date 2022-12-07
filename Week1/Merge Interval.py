class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #O(nlog n)-soritn and iterating
        #sort list of pairs via start val
        intervals.sort(key=lambda i:i[0])
        output=[intervals[0]] #for merged-to avoid edge case

        for start,end in intervals[1:]: #alrady added 1st so start from 1
            last=output[-1][1] #recent added & end val-> to know if it overlaps
            if start<=last: #if overlap , merge
                #set to max of itself w/ max last and current end
                output[-1][1]=max(last,end) 
                
            else:
                output.append([start,end]) #add interval to o/p ie leave it
        return output

        #max taken bcz [1,5] [2,4] -> [1,5]
        #[1,5] [7,8] -> [1,5],[7,8]