#include <vector>
#include <string>
#include <algorithm>
#include <climits>

class Solution {
public:
    std::string stoneGameIII(std::vector<int>& stoneValue) {
        int n = stoneValue.size();
        std::vector<int> dp(n + 1, 0);

        for (int i = n - 1; i >= 0; --i) {
            dp[i] = INT_MIN;
            int take_sum = 0;

            for (int x = 1; x <= 3 && i + x <= n; ++x) {
                take_sum += stoneValue[i + x - 1];
                dp[i] = std::max(dp[i], take_sum - dp[i + x]);
            }
        }

        if (dp[0] > 0) return "Alice";
        if (dp[0] < 0) return "Bob";
        return "Tie";
    }
};