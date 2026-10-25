
class Solution:
    def countMagicalPairs(self, s: str) -> int:
        n = len(s)
        M = s
        ans = 0

        for j in range(n - 1):
            left = [0] * (j + 1)
            seen = set()

            for i in range(j, -1, -1):
                seen.add(M[i])
                left[i] = len(seen)

            freq = [0] * 27
            for count in left:
                freq[count] += 1

            seen = set()
            for k in range(j + 1, n):
                seen.add(M[k])
                ans += freq[len(seen)]

        return ans
