#https://leetcode.com/problems/top-k-frequent-elements/description/
"""
Time complexity: O(n)
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a hashmap/dictionary to store frequency of each number in the array
        count = {}
        #create a freqeuncy buckets
        #where this will iterate each number in the range and 
        #create an empty list [] for each number
        frequency = [[] for i in range(len(nums) +1)]

        #count the frequency of each number
        #and store them in the count dictionary
        for n in nums:
            #if key found, return val that associated with n
            #if key not found, it returns the default value 0
            count[n] = 1 + count.get(n, 0)

        # populate the frequency buckets
        for n, c in count.items():
            frequency[c].append(n)

        output = []
        # iterate through the frequency buckets in reverse order
        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                output.append(n)
                #if collected k elements, return result
                if len(output) == k:
                    return output

