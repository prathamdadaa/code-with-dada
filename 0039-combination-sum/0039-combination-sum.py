class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()  # Sorting enables early pruning
        
        def backtrack(start: int, path: list[int], remaining: int):
            if remaining == 0:
                res.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break  # Stop search when candidate exceeds remaining target
                
                path.append(candidates[i])
                # Pass 'i' instead of 'i + 1' to allow reusing the current number
                backtrack(i, path, remaining - candidates[i])
                path.pop()  # Backtrack

        backtrack(0, [], target)
        return res