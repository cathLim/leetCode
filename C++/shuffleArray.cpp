https://leetcode.com/problems/shuffle-the-array/
class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        int j = 2 * n - 1;

        for (int i = 0; i < nums.size(); i++) {
            nums[i] = (nums[i] << 10) | nums[i + n]; // shift the value to left by 10 bits and store both values
        }

        for (int i = n - 1; i >= 0; i--) {
            // the expression 1 << 10 represents a left shift operation, where the number 1 is shifted to the left by 10 bits. 
            //this is to calculate the value of 2 raised to the power of 10
            // for example, 00000001 << 10 = 00100000 00000000 = 2^10 = 1024
            int y = nums[i] & ((1 << 10) - 1);
            int x = nums[i] >> 10;

            nums[j] = y;
            nums[j - 1] = x;
            j -= 2;
        }
        
        return nums;
    }
};
