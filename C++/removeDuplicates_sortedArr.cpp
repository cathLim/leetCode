//https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution{
    public:
    int removeDuplicates(vector<int>& nums)
    {
        //check the content of nums
        if(nums.size() == 0)
        {
            return 0;
        }

        int j=1; //to keep track of the position of non-duplicates element
        for(int i=1; i<nums.size(); i++)
        {
            //Check whether right value same as left value
            //If not, assign right value to 
            if(nums[i] != nums[i-1])
            {
                nums[j] = nums[i];
                j++;
            }
        }
        return j;
    }
}