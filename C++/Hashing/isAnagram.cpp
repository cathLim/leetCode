//https://leetcode.com/problems/valid-anagram/
/*
    using HashMap approach
    1. creates two hashmap, s and t
    2. compare both value
    3. make sure both have the same length

Time complexity: O(s+t)
Space complexity: O(s+t)
*/
class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) return false;
        
        unordered_map<char,int> smap;
        unordered_map<char,int> tmap;
        
        for(int i = 0; i < s.size(); i++){
            smap[s[i]]++;
            tmap[t[i]]++;
        }
        
        for(int i = 0; i < smap.size(); i++){
            if(smap[i] != tmap[i]) return false;
        }
        return true;
    }
};