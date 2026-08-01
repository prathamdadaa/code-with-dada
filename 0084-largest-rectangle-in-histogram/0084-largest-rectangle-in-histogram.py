class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = []  # Stores indices of histogram bars
        
        # Append a sentinel value (0) to flush remaining elements in stack at the end
        heights.append(0)
        
        for i, h in enumerate(heights):
            # Maintain monotonic non-decreasing stack
            while stack and heights[stack[-1]] > h:
                height_idx = stack.pop()
                height = heights[height_idx]
                
                # If stack is empty, width extends from index 0 to i
                width = i if not stack else i - stack[-1] - 1
                
                max_area = max(max_area, height * width)
                
            stack.append(i)
            
        return max_area