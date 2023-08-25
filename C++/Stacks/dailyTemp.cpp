
https://leetcode.com/problems/daily-temperatures/
/*
    Given array of temps, return an array w/ # of days until warmer
    Ex. temperature = [73,74,75,71,69,72,76,73] -> [1,1,4,2,1,1,0,0]

    Monotonic decreasing stack, at each day, compare increment from previous days

    Time: O(n)
    Space: O(n)
*/

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        
        // pair: [index, temp]
        stack<pair<int, int>> st;
        vector<int> result(n);
        
        for (int i = 0; i < n; i++) {
            int currentDay = i;
            int currentTemp = temperatures[i];
            
            while (!stk.empty() && stk.top().second < currentTemp) {
                int prevDay = stk.top().first;
                int prevTemp = stk.top().second;
                stk.pop();
                
                result[prevDay] = currentDay - prevDay;
            }
            
            st.push({currentDay, currentTemp});
        }
        
        return result;
    }
};
