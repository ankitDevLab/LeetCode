from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1=Counter(s)
        freq2=Counter(t)
        freq=freq1 if len(freq1)>len(freq2) else freq2
        freqf=freq1 if len(freq1)<=len(freq2) else freq2
        for i,j in freq.items():
            if freqf.get(i,-1)!=j:
                return False
        return True
                
        