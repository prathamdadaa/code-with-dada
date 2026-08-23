class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p = len(s) - 1
        length = 0
        
        # 1. Skip trailing spaces
        while p >= 0 and s[p] == ' ':
            p -= 1
            
        # 2. Count characters of the last word
        while p >= 0 and s[p] != ' ':
            length += 1
            p -= 1
            
        return length