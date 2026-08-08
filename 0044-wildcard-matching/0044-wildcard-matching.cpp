#include <string>

class Solution {
public:
    bool isMatch(std::string s, std::string p) {
        int s_idx = 0, p_idx = 0;
        int star_idx = -1, match_idx = -1;
        int s_len = s.length(), p_len = p.length();
        
        while (s_idx < s_len) {
            if (p_idx < p_len && (p[p_idx] == '?' || p[p_idx] == s[s_idx])) {
                s_idx++;
                p_idx++;
            } else if (p_idx < p_len && p[p_idx] == '*') {
                star_idx = p_idx;
                match_idx = s_idx;
                p_idx++;
            } else if (star_idx != -1) {
                p_idx = star_idx + 1;
                match_idx++;
                s_idx = match_idx;
            } else {
                return false;
            }
        }
        
        while (p_idx < p_len && p[p_idx] == '*') {
            p_idx++;
        }
        
        return p_idx == p_len;
    }
};