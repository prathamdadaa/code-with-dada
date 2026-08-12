class Solution {
public:
    double myPow(double x, int n) {
        long long N = n; // Cast to 64-bit to prevent overflow on -2^31
        if (N < 0) {
            x = 1.0 / x;
            N = -N;
        }

        double ans = 1.0;
        double current_product = x;

        while (N > 0) {
            if (N % 2 == 1) {
                ans *= current_product;
            }
            current_product *= current_product;
            N /= 2;
        }

        return ans;
    }
};