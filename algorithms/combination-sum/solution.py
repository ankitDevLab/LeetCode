class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(needle)
        i=0
        while i+n <= len(haystack):
            if needle == haystack[i:i+n]:
                return i
            i+=1
        return -1
        