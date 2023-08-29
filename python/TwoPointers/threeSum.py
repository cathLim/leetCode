#https://leetcode.com/problems/3sum/
#Using the same approach as twoSumII -> two pointers
"""
       _ + _ + _ = 0
       a   b   c

Set a as a fixed first value, work on b and c (two pointers approach)

1. First we sort the input array
2. Then, we utilise each num in the input array as a possible first value
(to set the first value, so that second and third value, we able to use the twoSumII two pointers approach )



Time complexity: O(nlogn) + O(n^2)
                which ~ O(n^2)
                because we sort the array which -> O(nlogn)
                and we use two loops -> O(n^2) ,
                where loop 1 use to tell us the 1st value
                and loop 2 use to solve 2sum problem

Space complexity might be O(1) or O(n) depends on the sorting algorithm as some might use extra memory
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    output.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return output
