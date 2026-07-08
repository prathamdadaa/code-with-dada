class Solution:
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        m = len(s)
        
        # 1. Prefix sum for the sum of digits
        pref_sum = [0] * (m + 1)
        for i in range(m):
            pref_sum[i + 1] = pref_sum[i] + int(s[i])
            
        # 2. Extract non-zero digits
        A = []
        for char in s:
            if char != '0':
                A.append(int(char))
                
        n = len(A)
        
        # 3. Precompute prefix values for the non-zero array A
        P = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = (P[i] * 10 + A[i]) % MOD
            
        # Precompute powers of 10
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        # 4. Map string indices to non-zero array indices safely
        next_nonzero = [-1] * m
        prev_nonzero = [-1] * m
        
        idx = 0
        for i in range(m):
            if s[i] != '0':
                prev_nonzero[i] = idx
                idx += 1
            else:
                prev_nonzero[i] = prev_nonzero[i - 1] if i > 0 else -1
                
        idx = n - 1
        for i in range(m - 1, -1, -1):
            if s[i] != '0':
                next_nonzero[i] = idx
                idx -= 1
            else:
                next_nonzero[i] = next_nonzero[i + 1] if i < m - 1 else -1

        # 5. Process each query
        ans = []
        for li, ri in queries:
            L = next_nonzero[li]
            R = prev_nonzero[ri]
            
            # If there are no non-zero digits in the range, or boundaries cross
            if L == -1 or R == -1 or L > R:
                ans.append(0)
            else:
                # Calculate x % MOD safely using prefix hashes
                length = R - L + 1
                x = (P[R + 1] - P[L] * pow10[length]) % MOD
                
                # Calculate sum of digits
                current_sum = pref_sum[ri + 1] - pref_sum[li]
                
                # Append answer (x * sum) % MOD
                ans.append((x * current_sum) % MOD)
                
        return ans