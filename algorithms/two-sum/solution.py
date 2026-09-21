class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results=[]
        def backtrack(index,current,remaining):
            if remaining==0:
                results.append(current.copy())
                return
            if remaining<0:
                return
            if index == len(candidates):
                return
            current.append(candidates[index])
            backtrack(index,current,remaining-candidates[index])
            current.pop()
            backtrack(index+1,current,remaining)
        backtrack(0,[],target)

        return results

        
        