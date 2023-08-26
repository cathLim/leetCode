#https://leetcode.com/problems/valid-anagram/
"""
    using HashMap approach
    1. creates two hashmap, s and t
    2. compare both value
    3. make sure both have the same length

Time complexity: O(s+t)
Space complexity: O(s+t)
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_S, count_T = {},{}

        for i in range(len(s)):
            count_S[s[i]] = 1 + count_S.get(s[i], 0)
            count_T[t[i]] = 1 + count_T.get(t[i], 0)

        for c in count_S:
            if count_S[c] != count_T.get(c,0):
                return False
        return True


