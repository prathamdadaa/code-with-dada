#include <string>
#include <vector>

class Solution {
public:
    std::string countAndSay(int n) {
        std::string s = "1";
        
        for (int step = 1; step < n; ++step) {
            std::string next_s = "";
            int i = 0;
            while (i < s.length()) {
                int count = 1;
                while (i + 1 < s.length() && s[i] == s[i + 1]) {
                    count++;
                    i++;
                }
                next_s += std::to_string(count) + s[i];
                i++;
            }
            s = next_s;
        }
        
        return s;
    }
};