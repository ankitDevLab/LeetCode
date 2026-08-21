class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        starts=0
        ends=0
        curr=0
        index={}
        for i in range(len(s)):
            if s[i] in index and index[s[i]] >= starts :
                starts=index[s[i]]+1
            ends+=1
            index[s[i]]=i

            r= ends - starts
            if curr <r:
                curr=r

        return curr