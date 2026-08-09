class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        # We don't need to check the last index (n - 1)
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            
            # Reached the end of the current jump range
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # Early stop if we can already reach or pass the last index
                if current_end >= n - 1:
                    break
                    
        return jumps