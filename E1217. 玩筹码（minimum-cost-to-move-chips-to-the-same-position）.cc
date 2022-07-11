class Solution {
public:
    // 遍历（统计奇数和偶数的数量）
    // 时间o(n) 空间O(1)
    int minCostToMoveChips(vector<int>& position) {
        int odd = 0, even = 0;
        for (int p : position) {
            if (p & 1) {
                ++odd;
            } else {
                ++even;
            }
        }
        return std::min(odd, even);
    }
};