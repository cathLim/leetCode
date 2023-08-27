
#Time complexity O(n)
#There are duplicates of initialise product =1, which not so good
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        current_num = [1]

        for i in range(1, len(nums)):
            product *= nums[i-1]
            current_num.append(product)
        
        product = 1
        for i in range(len(nums) -1, 0, -1):
            product *= nums[i]
            current_num[i-1] *= product
        return current_num
"""

#Alternative approach
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #create an array output of the same length as the input array nums
        #fill it with 1
        output = [1] * (len(nums))

        #this loop calculates the products to the left of each element
        #it starts from index 1, and set the value of output[i]
        #to be the product of all elements to the left of index i
        #e.g. 1 | 2 | 3 | 4 
"""
        For i = 1:

        output[1] = output[0] * nums[0] = 1 * 1 = 1
        For i = 2:

        output[2] = output[1] * nums[1] = 1 * 2 = 2
        For i = 3:

        output[3] = output[2] * nums[2] = 2 * 3 = 6

"""

        for i in range(1, len(nums)):
            output[i] = output[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output
