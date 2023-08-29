#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
Brute Force approach

   1 | 3 | 4 | 5 | 7 | 10 | 11   target =9

first we take 1 and added to the right value 3, 1 + 3 < 9
then we continuely added to the right value until 10, 1 + 10 > 9
since 1 + 10 exceed the target, we ignored the value after 10

After done for 1, we continue with number 3, with the same approach until we found 
4 + 5 = 9 

Downside:
Since this approach will go thru the whole array n times, where the length of array is n

Time complexity : O(n^2)

*******************************************************************************************
Implement a new approach with two pointers

    1 | 3 | 4 | 5 | 7 | 10 | 11   target =9
    ^                         ^
    |                         |

    now we have two pointers, left and right pointing to (l points to 1 and r points to 11)

    1 + 11 > 9 ; too huge
    we need to think of switching which pointers in order to lowering the totalSum

    If we switch the left pointer to right, which from value 1 to 3, 
    3 + 11 > 9; even huge number which is invalid

    so to increment the totalSum, we shift the right pointer to left
       to decrement the totalSum, we shift the left pointer to right

    By shifting the right pointer from 11 to 10
    1 + 10 > 9 ; too huge
    
    shift again from right to left (10 to 7)
    1 + 7 < 9 ; too small

    now, we shift from left to right (1 to 3)
    3 + 7 > 9 ;  too huge

    then, we shift again from right to left (7 to 5)
    3 + 5 < 9 ; too small

    this time, we shift from left to right (3 to 4)
    4 + 5 = 9 , we have got the same value as target

    then we return the position of left and right pointers by adding both of them 1, since leetcode ques starts from index 1 

Time complexity O (n)

"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            totalSum = numbers[l] + numbers[r]

            if totalSum > target:
                r -= 1
            elif totalSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
