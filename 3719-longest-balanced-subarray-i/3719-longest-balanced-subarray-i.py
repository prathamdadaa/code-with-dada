class Solution:
    def longestBalanced(self, nums):
        max_len = 0
        n = len(nums)
        
        for i in range(n):
            # Using sets to track unique even and odd numbers
            even_set = set()
            odd_set = set()
            
            for j in range(i, n):
                val = nums[j]
                if val % 2 == 0:
                    even_set.add(val)
                else:
                    odd_set.add(val)
                
                # Check if the number of distinct elements is balanced
                if len(even_set) == len(odd_set):
                    if (j - i + 1) > max_len:
                        max_len = j - i + 1
                    
        return max_len
