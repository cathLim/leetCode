#https://leetcode.com/problems/longest-repeating-character-replacement/
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0 
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

    """
    class Solution:
    def characterReplacement(self, s, k):
        counts = {}
        maxf = 0
        l = 0
        for r, ch in enumerate(s):
            counts[ch] = 1 + counts.get(ch, 0)
            maxf = max(maxf, counts[ch])
            if maxf + k < r - l + 1:
                counts[s[l]] -= 1
                l += 1

        return len(s) - l
    """

        