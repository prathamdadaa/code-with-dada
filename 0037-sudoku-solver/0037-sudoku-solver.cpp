#include <vector>

class Solution {
private:
    bool rows[9][10] = {false};
    bool cols[9][10] = {false};
    bool boxes[9][10] = {false};

    bool backtrack(std::vector<std::vector<char>>& board, int r, int c) {
        if (r == 9) return true; // Reached the end of the board
        if (c == 9) return backtrack(board, r + 1, 0); // Move to next row
        
        if (board[r][c] != '.') {
            return backtrack(board, r, c + 1); // Skip pre-filled cells
        }

        int box_idx = (r / 3) * 3 + (c / 3);

        for (int num = 1; num <= 9; ++num) {
            if (!rows[r][num] && !cols[c][num] && !boxes[box_idx][num]) {
                // Place digit
                board[r][c] = num + '0';
                rows[r][num] = cols[c][num] = boxes[box_idx][num] = true;

                if (backtrack(board, r, c + 1)) return true;

                // Backtrack
                board[r][c] = '.';
                rows[r][num] = cols[c][num] = boxes[box_idx][num] = false;
            }
        }

        return false;
    }

public:
    void solveSudoku(std::vector<std::vector<char>>& board) {
        // Initialize tracking arrays
        for (int r = 0; r < 9; ++r) {
            for (int c = 0; c < 9; ++c) {
                if (board[r][c] != '.') {
                    int num = board[r][c] - '0';
                    int box_idx = (r / 3) * 3 + (c / 3);
                    rows[r][num] = cols[c][num] = boxes[box_idx][num] = true;
                }
            }
        }
        backtrack(board, 0, 0);
    }
};