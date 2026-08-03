#include <string>
#include <vector>
#include <numeric>

class Solution {
public:
    std::string convert(std::string s, int numRows) {
        if (numRows == 1 || numRows >= s.length()) {
            return s;
        }

        std::vector<std::string> rows(numRows);
        int current_row = 0;
        bool going_down = false;

        for (char c : s) {
            rows[current_row] += c;

            if (current_row == 0 || current_row == numRows - 1) {
                going_down = !going_down;
            }

            current_row += going_down ? 1 : -1;
        }

        std::string result = "";
        for (const std::string& row : rows) {
            result += row;
        }

        return result;
    }
};