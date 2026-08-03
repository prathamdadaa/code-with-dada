#include <string>
#include <algorithm>

class Solution {
public:
    std::string longestPalindrome(std::string s) {
        if (s.empty()) return "";

        int start = 0, max_len = 0;

        auto expandAroundCenter = [&](int left, int right) {
            while (left >= 0 && right < s.length() && s[left] == s[right]) {
                left--;
                right++;
            }
            return right - left - 1;
        };

        for (int i = 0; i < s.length(); ++i) {
            int len1 = expandAroundCenter(i, i);     // Odd length
            int len2 = expandAroundCenter(i, i + 1); // Even length

            int len = std::max(len1, len2);
            if (len > max_len) {
                max_len = len;
                start = i - (len - 1) / 2;
            }
        }

        return s.substr(start, max_len);
    }
};