class Solution {
public:
    // 排序
    // 时间O(nlogn) 空间O(logn)
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        std::sort(arr.begin(), arr.end());
        int min_abs = 2000001;
        vector<vector<int>> ans;
        for (int i = 1; i < arr.size(); ++i) {
            if (arr[i] - arr[i-1] <= min_abs) {
                if (arr[i] - arr[i-1] < min_abs) {
                    min_abs = arr[i] - arr[i-1];
                    ans.clear();
                }
                ans.emplace_back(vector<int> ({arr[i-1], arr[i]}));
            }
        }
        return ans;
    }
};