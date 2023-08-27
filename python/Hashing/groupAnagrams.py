#https://leetcode.com/problems/group-anagrams/description/

"""
Time complexity: O(mnlogn)
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create an empty hashmap/dictionary
        output = {}

        #to group anagram
        #take each strings in the array and sort them
        for string in strs:
            #sorts the char in string variable
            #joins them back tgt to create a new string with sorted order characters
            sorted_string = ''.join(sorted(string))

            #check whether the sorted_string is already a key in output
            #if sorted_string is not present as a key of output dictionary
            #add sorted _string as a new key of output dictionary
            #assign an empty list as a value which corresponds to the key
            if sorted_string not in output:
                output[sorted_string] = []

            output[sorted_string].append(string)

        #return a list of values containing the values of output dictionary
        return list(output.values())
