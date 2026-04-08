class Solution {
public:

    int orangesRotting(vector<vector<int>>& grid) {
        int ROWS = grid.size();
        int COLS = grid[0].size();
        queue<pair<int,int>> q; // 
        int fresh = 0;
        int time = 0; 
        for (int r =0; r < ROWS; r++){
            for (int c = 0; c < COLS; c++){
                if (grid[r][c] == 2){
                    q.push({r,c});
                }
                if (grid[r][c] == 1){
                    fresh+=1;
                }
            }
        }

        std::vector<pair<int,int>> directions = {{0,1}, {1,0}, {0,-1}, {-1,0}};
        while (!q.empty() && fresh > 0){
            int qSize = q.size();
            for (int i = 0; i < qSize; i++){
                auto top = q.front();
                q.pop();
                int r = top.first;
                int c = top.second;
                for (auto [dr,dc]: directions){
                    int nr = r+dr;
                    int nc = c+dc;
                    if (nr < 0 || nr >= ROWS || nc <0 || nc>=COLS || grid[nr][nc]!=1){
                        continue;
                    }
                    grid[nr][nc] = 2;
                    q.push({nr,nc});
                    fresh --;
                }
            }
            time+=1;

        }
        return fresh == 0 ? time : -1;
    }
};