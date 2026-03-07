class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        l=0
        maxlen=0
        seen=set()
        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            maxlen=max(maxlen,r-l+1)
        return maxlen

        

        

        
        