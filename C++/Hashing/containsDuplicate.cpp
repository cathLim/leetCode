//https://leetcode.com/problems/contains-duplicate/
/*
    Given int array, return true if any value appears at least twice
    Ex. nums = [1,2,3,1] -> true, nums = [1,2,3,4] -> false

    If the number has been seen previously, then it has a duplicate. Otherwise, insert it into the hash set.

    Time: O(n)
    Space: O(n)
*/
//Uses a hash table to store its element

class Solution:
public:
    bool containsDuplicates(vector<int>& nums){
        unordered_set<int> s;

        for(int i=0; i<nums.size(); i++)
        {
            if(s.find(nums[i] != s.end()))
            {
                return true;
            }
            s.insert(nums[i]);
        }
    return false;
    }