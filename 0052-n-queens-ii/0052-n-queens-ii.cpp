class Solution {
public:
    int totalNQueens(int n) {
        int count = 0;
        int limit = (1 << n) - 1; // Full row mask of 1s
        
        auto backtrack = [&](auto& self, int cols, int diag1, int diag2) -> void {
            if (cols == limit) {
                count++;
                return;
            }
            
            // Available spots are 0s in (cols | diag1 | diag2), so invert and mask
            int avail = limit & ~(cols | diag1 | diag2);
            
            while (avail > 0) {
                int pick = avail & -avail; // Lowest set bit
                avail -= pick;
                
                self(self, cols | pick, (diag1 | pick) << 1, (diag2 | pick) >> 1);
            }
        };
        
        backtrack(backtrack, 0, 0, 0);
        return count;
    }
};