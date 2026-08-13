#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> results;
        vector<string> board(n, string(n, '.'));
        
        unordered_set<int> cols;
        unordered_set<int> posDiags; // r + c
        unordered_set<int> negDiags; // r - c

        auto backtrack = [&](auto& self, int r) -> void {
            if (r == n) {
                results.push_back(board);
                return;
            }

            for (int c = 0; c < n; ++c) {
                if (cols.count(c) || posDiags.count(r + c) || negDiags.count(r - c)) {
                    continue;
                }

                cols.insert(c);
                posDiags.insert(r + c);
                negDiags.insert(r - c);
                board[r][c] = 'Q';

                self(self, r + 1);

                cols.erase(c);
                posDiags.erase(r + c);
                negDiags.erase(r - c);
                board[r][c] = '.';
            }
        };

        backtrack(backtrack, 0);
        return results;
    }
};