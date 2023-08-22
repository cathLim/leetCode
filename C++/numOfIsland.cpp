class Solution {
public:
    void dfs(vector<vector<char>>& grid, int r, int c) {
        // This is a base case for recursion
        // If the rows or cols out of range || grid[row][col] != 1, it will return
        if (r < 0 || r >= grid.size() || c < 0 || c >= grid[0].size() || grid[r][c] != '1') 
        {
            return;
        }
        
        //This is an update step
        // to mark the value of grid[r][c] to 2
        // this indicates that the they has been visited
        grid[r][c] = '2';
        
        // DFS function is recursively call for adjacent rows and cols
        dfs(grid, r + 1, c); // Move down
        dfs(grid, r - 1, c); // Move up
        dfs(grid, r, c + 1); // Move right
        dfs(grid, r, c - 1); // Move left
    }
    
    int numIslands(vector<vector<char>>& grid) 
    {
        int islandCount = 0;
        
        // Traverse each vertices in the grid
        for (int r = 0; r < grid.size(); r++) 
        {
            for (int c = 0; c < grid[0].size(); c++) {
                if (grid[r][c] == '1') 
                {
                    islandCount++;
                    dfs(grid, r, c);
                }
            }
        }
        
        return islandCount;
    }
};