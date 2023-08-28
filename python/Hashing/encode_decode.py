#https://www.lintcode.com/problem/659/
#Time complexity: O(n), where n is the total nums of char given to us in the list of words
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        #take the length of string and transform them into a single string
        #delimiter "#" is used to separate between two strings
        output=""
        for s in strs:
            output += str(len(s)) + "#" + s
        return output
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        #create an array to store our decoded list of strings and 
        #a pointer i to tell us what position we are at
        output, i = [], 0

        #iterate character by character
        #while pointer i still inbound
        #read character by character, decoding each string
        while i < len(s):
            j = i
            #haven't reached the second string
            while s[j] != "#":
                j += 1
            # Length of the string from the first index i to the index before j
            # For example, consider the string "5#hello6#worlds"
            # Starting from index i which is 0, we loop until we find the pound sign '#'.
            # The position of the pound sign should not be included in the length calculation.
            # At j=1, we find the '#' sign. We exclude this position while calculating the length.
            length = int(s[i:j])

            # Then we append the substring to the output array.
            # j+1 indicates the position right after the '#'.
            # j+1+length represents the position up to which we want to extract the substring.
            output.append(s[j+1 : j + 1 + length])
            i = j + 1 + length
        return output