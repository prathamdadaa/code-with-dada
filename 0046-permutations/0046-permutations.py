class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        def backtrack(current_perm, used):
            # Base case: completed a valid permutation
            if len(current_perm) == len(nums):
                res.append(current_perm[:])  # Append a copy
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    # Choose
                    used[i] = True
                    current_perm.append(nums[i])
                    
                    # Explore
                    backtrack(current_perm, used)
                    
                    # Backtrack (Unchoose)
                    current_perm.pop()
                    used[i] = False
        
        backtrack([], [False] * len(nums))
        return res