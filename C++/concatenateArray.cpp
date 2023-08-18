class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        std::vector<int> ans;

        //concatenate of the array by itself twice
        for(int i=0; i<2; i++)
        {
            for(n : nums)
            {
                ans.push_back(n);
            }

        }
        return ans;
    }
};