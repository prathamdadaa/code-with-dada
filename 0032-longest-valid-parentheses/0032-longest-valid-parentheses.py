class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]  # Base index marker for boundary calculations
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # Current ')' serves as the new boundary marker
                    stack.append(i)
                else:
                    # Valid substring found from stack[-1] + 1 to i
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len