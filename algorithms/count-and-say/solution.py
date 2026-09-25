class Solution:
    def countAndSay(self, n: int) -> str:
        def newbuild(rle):
            res=[]
            prev=rle[0]
            count=0
            for i in rle:
                if prev== i:
                    count+=1
                else:
                    res.extend([str(count),prev])
                    prev=i
                    count=1
            res.extend([str(count),prev])
            return "".join(res)
        final="1"
        for i in range(n-1):
            final=newbuild(final)
        return final



        