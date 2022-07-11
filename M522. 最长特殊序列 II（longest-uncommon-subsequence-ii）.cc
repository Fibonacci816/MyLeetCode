class Solution {
public:
    // 枚举 + 判断
    // 时间O(n^2 · l) 空间O(1)，l 为字符串平均长度
    int findLUSlength(vector<string>& strs) {
        // 判断 s 是否为 t 的子序列
        auto is_subseq = [](const string& s, const string& t) {
            int pt_s = 0, pt_t = 0;
            while (pt_s < s.size() && pt_t < t.size()) {
                if (s[pt_s] == t[pt_t++]) {
                    ++pt_s;
                }
            }
            return pt_s == s.size();
        };

        int ans = -1;
        for (int i = 0; i < strs.size(); ++i) {
            bool flag = true;
            for (int j = 0; j < strs.size(); ++j) {
                if (i != j && is_subseq(strs[i], strs[j])) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                ans = max(ans, static_cast<int>(strs[i].size()));
            }
        }
        return ans;
    }
};