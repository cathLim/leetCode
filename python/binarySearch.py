https://leetcode.com/problems/binary-search/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L,R =0, len(nums)-1

        #Make sure that L and R ptr are within the range 
        while(L<=R):
            M = (L+R)//2
            if target > nums[M]:
                L = M+1
            elif target < nums[M]:
                R = M-1
            else:
                return M
        return -1
