class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reachable = 0
        target = len(nums) - 1
        
        for i, jump in enumerate(nums):
            # If the current index is beyond the maximum reachable index, fail early
            if i > max_reachable:
                return False
            
            # Update the furthest index we can reach
            max_reachable = max(max_reachable, i + jump)
            
            # Optional optimization: stop early if we can already reach the end
            if max_reachable >= target:
                return True
                
        return True