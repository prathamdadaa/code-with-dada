from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)
        
        if s_len < total_len:
            return []
        
        word_counts = Counter(words)
        result = []
        
        # Run sliding window for each offset from 0 to word_len - 1
        for i in range(word_len):
            left = i
            right = i
            seen = Counter()
            count = 0  # Number of valid words matched in current window
            
            while right + word_len <= s_len:
                # Get the next word chunk
                word = s[right:right + word_len]
                right += word_len
                
                if word in word_counts:
                    seen[word] += 1
                    count += 1
                    
                    # If we have too many instances of `word`, shrink from the left
                    while seen[word] > word_counts[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    # If window size matches total words required, record index
                    if count == num_words:
                        result.append(left)
                else:
                    # Invalid word encounter: reset window completely
                    seen.clear()
                    count = 0
                    left = right
                    
        return result