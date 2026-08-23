import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Create a list of numbers to select from: [1, 2, ..., n]
        numbers = [str(i) for i in range(1, n + 1)]
        
        # Precompute factorials: factorials[i] = i!
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i - 1] * i
            
        # Convert k to 0-based index
        k -= 1
        
        result = []
        
        for i in range(n - 1, -1, -1):
            # Block size for the current position is (i)!
            fact = factorials[i]
            
            # Determine which number to pick
            index = k // fact
            result.append(numbers.pop(index))
            
            # Update k for the remaining subgroup
            k %= fact
            
        return "".join(result)