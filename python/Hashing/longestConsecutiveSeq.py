#https://leetcode.com/problems/longest-consecutive-sequence
"""
Given    100 | 4 | 200 | 1 | 3 | 2

1. we check for the first value 100
    -is it a start of sequence? yes, create a sequence of 100
    100 ->
    -is there any left neighbour? 99? no not exist
    -is there any right neightbout? 101? no not exist
 then stop the sequence since there is no left or right neighbour to continue

2. next, we check for the second value 4
    -is it a start of sequence? no, so we will not consider to make a range for it

3. next, we check for the third value 200
    -is it a start of sequence? yes, create a sequence of 200
    200->
    -is there any left neighbour? 199? no not exist
    -is there any right neighbout? 201? no not exist
then stop the sequence since there is no left or right neighbour to continue

4. next, we check for the fourth value 1
    -is it a start of sequence? yes, create a sequence of 1
    1->
    -is there any left neighbour? 0? no not exist
    -is there any right neightbour? 2?  yes exist
    continue the sequence by adding 2
    1->2

    -is there any left neighbour for 2? 1? yes exist
    -is there any right neighbour for 2? 3? yes exist
    continue the sequence by adding 3
    1->2->3->

    -is there any left neighbour for 3? 2? yes exist
    -is there any right neighbour for 3? 4? yes exist
    continue the sequence by adding 4
    1->2->3->4->

    -is there any left neighbour for 4? 3? yes exist
    -is there any right neighbour for 4? 5? no not exist
then stop the sequence since there is no left or right neighbour to continue

5. next, we check for the fifth value 3 and subsequently 2


Time complexity = O(n)
Memory complexity = O(n) , since we using a set
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #create a set from the initial array nums
        numSet = set(nums)

        #keep track the longest of sequence
        longestSeq = 0

        #iterate every number in array
        for n in numSet:
            #check is it the start of a sequence
            #check is it contains any left neighbour
            if(n - 1) not in numSet:
                length = 1
                #check is it contains any right neighbour
                while(n + length) in numSet:
                    length += 1
                longestSeq = max(length, longestSeq)
        return longestSeq
