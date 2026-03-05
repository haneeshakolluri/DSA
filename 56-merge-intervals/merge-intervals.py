class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        res=[]
        intervals.sort()
        current=intervals[0]
        for i in range(1,n):
            if current[1]>=intervals[i][0]:
                current[1]=max(current[1],intervals[i][1])
            else:
                res.append(current)
                current = intervals[i]
        res.append(current)
        return res
            





        