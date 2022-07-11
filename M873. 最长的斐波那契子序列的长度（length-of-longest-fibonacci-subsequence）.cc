class Solution {
public:
    // dp
    // 时间O(n^2) 空间O(n)
    int lenLongestFibSubseq(vector<int>& arr) {
        unordered_map<int, int> idx;
        for (int i = 0; i < arr.size(); ++i) {
            idx[arr[i]] = i;
        }
        int n = arr.size();
        int dp[n][n];
        memset(dp, 0, sizeof(dp));
        int ans = 0;
        for (int i = arr.size() - 1; i >= 0; --i) {
            for (int j = i + 1; j < arr.size(); ++j) {
                if (arr[i] + arr[j] > arr[arr.size()-1]) break;
                if (idx.count(arr[i]+arr[j])) {
                    int k = idx[arr[i]+arr[j]];
                    dp[i][j] = max(3, 1 + dp[j][k]);
                    ans = max(ans, dp[i][j]);
                }
            }
            
        }
        return ans;
    }
};