#include <string>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        std::unordered_map<char, int> seen;
        int left = 0;
        int max_len = 0;

        for (int right = 0; right < s.length(); ++right) {
            char current_char = s[right];

            // Move left pointer past the last seen position of current_char
            if (seen.find(current_char) != seen.end() && seen[current_char] >= left) {
                left = seen[current_char] + 1;
            }

            seen[current_char] = right;
            max_len = std::max(max_len, right - left + 1);
        }

        return max_len;
    }
};