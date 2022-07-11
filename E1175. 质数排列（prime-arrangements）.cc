class Solution {
public:
    // 判断质数 + 排列组合
    // 时间O(n^(3/2)) 空间O(1)
    int numPrimeArrangements(int n) {
        auto is_prime = [](int n) {
            if (n < 2) return 0;
            for (int i = 2; i * i <= n; ++i) {
                if (n % i == 0) return 0;
            }
            return 1;
        };
        
        int prime_num = 0;
        for (int i = 1; i <= n; ++i) {
            prime_num += is_prime(i);
        }
        int MOD = pow(10, 9) + 7;

        auto factorial = [MOD](int n) {
            long ans = 1;
            for (int i = 1; i <= n; ++i) {
                ans = ans * i % MOD;
            }
            return ans;
        };
        
        return factorial(prime_num) * factorial(n - prime_num) % MOD;
    }
};