class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        val = 1
        
        while val <= n * n:
            # 1. Fill top row (left -> right)
            for col in range(left, right + 1):
                matrix[top][col] = val
                val += 1
            top += 1
            
            # 2. Fill right column (top -> bottom)
            for row in range(top, bottom + 1):
                matrix[row][right] = val
                val += 1
            right -= 1
            
            # 3. Fill bottom row (right -> left)
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = val
                val += 1
            bottom -= 1
            
            # 4. Fill left column (bottom -> top)
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = val
                val += 1
            left += 1
            
        return matrix