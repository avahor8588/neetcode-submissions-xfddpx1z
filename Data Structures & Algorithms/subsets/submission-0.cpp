class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> path;
        dfs(nums, 0, path);
        return res;
    }
    void dfs(vector<int>& nums, int i, vector<int>& path){
        if (i == nums.size()){
            res.push_back(path);
            return;
        }

        path.push_back(nums[i]);
        dfs(nums, i+1, path);
        path.pop_back();
        dfs(nums, i+1, path);

    }

    vector<vector<int>> res;
};