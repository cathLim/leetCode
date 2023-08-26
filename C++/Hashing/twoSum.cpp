/*
    Given array of int & target, return indices of 2 nums that add up to get target
    For e.g. nums = [2,7,11,15] & target = 9 -> [0,1], 2 + 7 = 9

    At each num, calculate complement, if exists in hash map then return

    Time: O(n)
    Space: O(n)
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        unordered_map<int, int> m; // val -> index

        for (int i = 0; i < n; i++) {
            int compliment = target - nums[i];
            if (m.find(compliment) != m.end()) {
                return {m[compliment], i};
            }
            m.insert({nums[i], i});
        }
        return {};
    }
};
