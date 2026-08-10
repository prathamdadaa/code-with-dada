from collections import Counter

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        counter = Counter(nums)
        
        def backtrack(comb):
            # Base case: valid permutation formed
            if len(comb) == len(nums):
                res.append(comb[:])
                return
            
            for num in counter:
                if counter[num] > 0:
                    # Choose
                    counter[num] -= 1
                    comb.append(num)
                    
                    # Explore
                    backtrack(comb)
                    
                    # Backtrack (Unchoose)
                    comb.pop()
                    counter[num] += 1
                    
        backtrack([])
        return res