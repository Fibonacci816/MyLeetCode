class Solution {
unordered_map<int, int> b2w;
int bound;

public:
    // 哈希影射
    // 时间 init: O(m) pick: O(1) 空间O(m)
    Solution(int n, vector<int>& blacklist) {
        bound = n - blacklist.size();
        unordered_set<int> black;
        for (int b : blacklist) {
            if (b >= bound) {
                black.emplace(b);
            }
        }
        int w = bound;
        for (int b : blacklist) {
            if (b < bound) {
                while (black.count(w++));
                b2w[b] = w - 1;
            }
        }
    }
    
    int pick() {
        int x = rand() % bound;
        return b2w.count(x) ? b2w[x] : x;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(n, blacklist);
 * int param_1 = obj->pick();
 */