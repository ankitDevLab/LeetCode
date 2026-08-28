class Solution:
    def isValid(self, s: str) -> bool:
        valid=[]
        opening=["{","[","("]
        closing=["}","]",")"]

        for i in s:
            if i in opening:
                valid.append(i)
            else:
                if not valid:
                    return False
                last=valid.pop()
                idx=opening.index(last)
                if i!=closing[idx]:
                    return False
        return len(valid)==0
        