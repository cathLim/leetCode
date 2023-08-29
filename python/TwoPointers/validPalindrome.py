#https://leetcode.com/problems/valid-palindrome/

"""
Conditions:
1. Ignoring cases
2. Read the same forward and backward
3. Remove all non-alphanumberic character

Two solutions for this ques:
************
Solution 1:
************

1. We first remove all the non-alphanumeric char from the input string by using python built-in function, .isalnum() to only store alphanumeric character and make sure that it is lowercase, .lower()

2. Next,we compare the given string with reverse string. In other words, we creates a new string that is reverse and compares it with our original given string. If both are same, continue, else return false.

Downside: 
What if we are not allowed to use any built in function or using any extra memory?
From the above case, we have using extra memory by creating a new reverse string, which affect our space complexity.

***********
Solution 2
***********
This approach uses two pointers: left (l) and right (r)

Without using any extra memory 
Space complexity : O(1)

Without using built in function to remove the non-alphanumeric characters
Time complexity : O(n), as we still need to go thru the whole size of string

1. First, we compare character of l and r pointers
2. If yes, then we shift the pointers,

    l->            <-r

   then we can continue to check thru the string and make sure that the character are equal
3. If not equal, then we return false

When to stop?
We uses two pointers and go thru the whole string, until they meet at the middle
"""

#Solution 1:
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        outputStr = ""

        for c in s:
            if c.isalnum():
                outputStr += c.lower()
        return outputStr == outputStr[::-1]
"""

#Solution 2:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        #outer while loop use to check have they meet each other yet
        while l < r:
            #inner while loop use to check whether left and right pointers are out of bound
            while l < r and not self.isAlphaNum(s[l]):
                #increment the left pointer, as it moves to the right side
                l += 1
            while l < r and not self.isAlphaNum(s[r]):
                #decrement the right point, as it moves to the left side
                r -= 1

            if(s[l].lower() != s[r].lower()):
                return False
        l, r = l + 1, r - 1
        return True

    #create an alphanumeric function
    def isAlphaNum(self, c):
        #ord() is a function to get ASCII value in python

        #Three conditions:
        #1. Compare they are upper case character or not
        #2. check lower case character
        #3. Check digits
        return(
            (ord('A') <= ord(c) <= ord('Z')) or
            (ord('a') <= ord(c) <= ord('z')) or
            (ord('0') <= ord(c) <= ord('9'))
        )
