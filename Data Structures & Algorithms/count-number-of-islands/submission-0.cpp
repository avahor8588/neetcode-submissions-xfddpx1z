class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int res = 0;
        for (int i = 0; i < grid.size(); i++ ){
            for (int j = 0; j < grid[0].size(); j++){
                if (grid[i][j] == '1'){
                    dfs(i, j, grid);
                    res++;
                }

            }
        }
        return res;
        
    }
    void dfs(int r, int c, vector<vector<char>>& grid){
        if (r < 0 || r >= grid.size() || c < 0 || c >= grid[0].size() || grid[r][c] == '0'){
            return;
        }
        grid[r][c] = '0';

        dfs(r, c+1, grid);
        dfs(r, c-1, grid);
        dfs(r-1,c,grid);
        dfs(r+1,c, grid);

    }
};