https://leetcode.com/problems/concatenation-of-array/
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = []

        #concatenation of two nums arrays, x=2
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans
