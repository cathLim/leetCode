#https://leetcode.com/problems/contains-duplicate/
class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()

        #this will go thru every value in the input array nums
        for n in nums:
            if n in hashset: #check duplicates
                return True
        hashset.add(n)
    return false
