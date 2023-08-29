#https://leetcode.com/problems/container-with-most-water/

"""
Brute Force Approach
     
    | 
    |          |
    |          |     
    |          |    |
    |          |    |
    |          |    |       |    
    |          |    |   |   |
    |          |    |   |   |
    |______|___|____|___|___|__________

           ^   ^
           |   |
        left   right

1. left pointer go thru every single indices of height
2. right pointer go thru at the position of l + 1 which until the end of the height
3. then using the area = width * height to calculate the area

where width = r - l
      height = min height (because no matter how tall our left/right pointer is, water will also split out if one of the pointer contains minimum height)

******************************************************************************************
Better appraoch:

Using two pointers method.

    | 
    |          |            7                            Max Area
    |          |            |
    |          |    |       |                         |-------------------|
    |          |    |       |                         | 1*4 = 4           |
    |          |    |       |                         | 7*4 = 28          |
    |      1   |    |   |   |                         |                   |
    |          |    |   |   |
    |______|___|____|___|___|__________

           ^ -> ^           ^
           |    |           |
        left   left        right


Area = width * height

"""
        
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        output = 0

        while l < r:
            output = max(output, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
            
        return output
