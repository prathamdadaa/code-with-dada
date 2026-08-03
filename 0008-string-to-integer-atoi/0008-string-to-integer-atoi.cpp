#include <string>
#include <climits>

class Solution {
public:
    int myAtoi(std::string s) {
        int i = 0;
        int n = s.length();
        
        // 1. Skip leading whitespaces
        while (i < n && s[i] == ' ') {
            i++;
        }
        
        if (i >= n) return 0;
        
        // 2. Check optional sign
        int sign = 1;
        if (s[i] == '-') {
            sign = -1;
            i++;
        } else if (s[i] == '+') {
            i++;
        }
        
        // 3. Read digits and check bounds
        int res = 0;
        while (i < n && std::isdigit(s[i])) {
            int digit = s[i] - '0';
            
            // Overflow check
            if (res > INT_MAX / 10 || (res == INT_MAX / 10 && digit > 7)) {
                return (sign == 1) ? INT_MAX : INT_MIN;
            }
            
            res = res * 10 + digit;
            i++;
        }
        
        return sign * res;
    }
};